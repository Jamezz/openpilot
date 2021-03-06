#!/usr/bin/env python
import numpy as np
from selfdrive.can.parser import CANParser
from .interface import CanBus

from cereal import car
from common.realtime import sec_since_boot

import zmq
from selfdrive.services import service_list
import selfdrive.messaging as messaging
import math

NUM_TARGETS_MSG = 1120
SLOT_1_MSG = NUM_TARGETS_MSG + 1
NUM_SLOTS = 20

# Actually it's 0x47f, but can parser only reports
# messages that are present in DBC
LAST_RADAR_MSG = NUM_TARGETS_MSG + NUM_SLOTS

def create_radard_can_parser(canbus):
  # C1A-ARS3-A by Continental
  dbc_f = 'gm_global_a_object'
  radar_targets = range(SLOT_1_MSG, SLOT_1_MSG + NUM_SLOTS)
  signals = zip(['LRRNumObjects'] +
                ['TrkRange'] * NUM_SLOTS + ['TrkRangeRate'] * NUM_SLOTS +
                ['TrkRangeAccel'] * NUM_SLOTS + ['TrkAzimuth'] * NUM_SLOTS +
                ['TrkWidth'] * NUM_SLOTS + ['TrkObjectID'] * NUM_SLOTS,
                [NUM_TARGETS_MSG] + radar_targets * 6,
                [0] + [0.0] * NUM_SLOTS + [0.0] * NUM_SLOTS +
                [0.0] * NUM_SLOTS + [0.0] * NUM_SLOTS +
                [0.0] * NUM_SLOTS + [0] * NUM_SLOTS)

  checks = []

  return CANParser(dbc_f, signals, checks, canbus.obstacle)

class RadarInterface(object):
  def __init__(self):
    # radar
    self.pts = {}
    self.track_id = 0
    self.num_targets = 0

    self.delay = 0.0  # Delay of radar

    canbus = CanBus()
    print "Using %d as obstacle CAN bus ID" % canbus.obstacle
    self.rcp = create_radard_can_parser(canbus)

    context = zmq.Context()
    self.logcan = messaging.sub_sock(context, service_list['can'].port)

  def update(self):
    updated_messages = set()
    while 1:
      tm = int(sec_since_boot() * 1e9)
      updated_messages.update(self.rcp.update(tm, True))
      if LAST_RADAR_MSG in updated_messages:
        break

    ret = car.RadarState.new_message()
    errors = []
    if not self.rcp.can_valid:
      errors.append("notValid")
    ret.errors = errors

    currentTargets = set()
    if self.rcp.vl[NUM_TARGETS_MSG]['LRRNumObjects'] != self.num_targets:
      self.num_targets = self.rcp.vl[NUM_TARGETS_MSG]['LRRNumObjects']

    # Not all radar messages describe targets,
    # no need to monitor all of the sself.rcp.msgs_upd
    for ii in updated_messages:
      if ii == NUM_TARGETS_MSG:
        continue

      if self.num_targets == 0:
        break

      cpt = self.rcp.vl[ii]
      # Zero distance means it's an empty target slot
      if cpt['TrkRange'] > 0.0:
        targetId = cpt['TrkObjectID']
        currentTargets.add(targetId)
        if targetId not in self.pts:
          self.pts[targetId] = car.RadarState.RadarPoint.new_message()
          self.pts[targetId].trackId = targetId
        distance = cpt['TrkRange']
        self.pts[targetId].dRel = distance # from front of car
        # From driver's pov, left is positive
        deg_to_rad = np.pi/180.
        self.pts[targetId].yRel = math.sin(deg_to_rad * cpt['TrkAzimuth']) * distance
        self.pts[targetId].vRel = cpt['TrkRangeRate']
        self.pts[targetId].aRel = float('nan')
        self.pts[targetId].yvRel = float('nan')

    for oldTarget in self.pts.keys():
      if not oldTarget in currentTargets:
        del self.pts[oldTarget]

    ret.points = self.pts.values()
    return ret

if __name__ == "__main__":
  RI = RadarInterface()
  while 1:
    ret = RI.update()
    print(chr(27) + "[2J")
    print ret



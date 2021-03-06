class HONDA:
  CIVIC = "HONDA CIVIC 2016 TOURING"
  ACURA_ILX = "ACURA ILX 2016 ACURAWATCH PLUS"
  CRV = "HONDA CR-V 2016 TOURING"
  ODYSSEY = "HONDA ODYSSEY 2018 EX-L"
  ACURA_RDX = "ACURA RDX 2018 ACURAWATCH PLUS"
  PILOT = "HONDA PILOT 2017 TOURING"


class TOYOTA:
  PRIUS = "TOYOTA PRIUS 2017"
  RAV4H = "TOYOTA RAV4 2017 HYBRID"
  RAV4 = "TOYOTA RAV4 2017"
  COROLLA = "TOYOTA COROLLA 2017"
  LEXUS_RXH = "LEXUS RX HYBRID 2017"

class GM:
  VOLT = "CHEVROLET VOLT PREMIER 2017"

_DEBUG_ADDRESS = {1880: 8}   # reserved for debug purposes

_FINGERPRINTS = {
  HONDA.ACURA_ILX: [{
    1024L: 5, 513L: 6, 1027L: 5, 1029L: 8, 929L: 4, 1057L: 5, 777L: 8, 1034L: 5, 1036L: 8, 398L: 3, 399L: 7, 145L: 8, 660L: 8, 985L: 3, 923L: 2, 542L: 7, 773L: 7, 800L: 8, 432L: 7, 419L: 8, 420L: 8, 1030L: 5, 422L: 8, 808L: 8, 428L: 8, 304L: 8, 819L: 7, 821L: 5, 57L: 3, 316L: 8, 545L: 4, 464L: 8, 1108L: 8, 597L: 8, 342L: 6, 983L: 8, 344L: 8, 804L: 8, 1039L: 8, 476L: 4, 892L: 8, 490L: 8, 1064L: 7, 882L: 2, 884L: 7, 887L: 8, 888L: 8, 380L: 8, 1365L: 5,
    # sent messages
    0xe4: 5, 0x1fa: 8, 0x200: 6, 0x30c: 8, 0x33d: 5,
  }],
  HONDA.ACURA_RDX: [{
    57L: 3, 145L: 8, 229L: 4, 308L: 5, 316L: 8, 342L: 6, 344L: 8, 380L: 8, 392L: 6, 398L: 3, 399L: 6, 404L: 4, 420L: 8, 422L: 8, 426L: 8, 432L: 7, 464L: 8, 474L: 5, 476L: 4, 487L: 4, 490L: 8, 506L: 8, 542L: 7, 545L: 4, 597L: 8, 660L: 8, 773L: 7, 777L: 8, 780L: 8, 800L: 8, 804L: 8, 808L: 8, 819L: 7, 821L: 5, 829L: 5, 882L: 2, 884L: 7, 887L: 8, 888L: 8, 892L: 8, 923L: 2, 929L: 4, 963L: 8, 965L: 8, 966L: 8, 967L: 8, 983L: 8, 985L: 3, 1024L: 5, 1027L: 5, 1029L: 8, 1033L: 5, 1034L: 5, 1036L: 8, 1039L: 8, 1057L: 5, 1064L: 7, 1108L: 8, 1365L: 5, 1424L: 5, 1729L: 1
  }],
  HONDA.CIVIC: [{
    1024L: 5, 513L: 6, 1027L: 5, 1029L: 8, 777L: 8, 1036L: 8, 1039L: 8, 1424L: 5, 401L: 8, 148L: 8, 662L: 4, 985L: 3, 795L: 8, 773L: 7, 800L: 8, 545L: 6, 420L: 8, 806L: 8, 808L: 8, 1322L: 5, 427L: 3, 428L: 8, 304L: 8, 432L: 7, 57L: 3, 450L: 8, 929L: 8, 330L: 8, 1302L: 8, 464L: 8, 1361L: 5, 1108L: 8, 597L: 8, 470L: 2, 344L: 8, 804L: 8, 399L: 7, 476L: 7, 1633L: 8, 487L: 4, 892L: 8, 490L: 8, 493L: 5, 884L: 8, 891L: 8, 380L: 8, 1365L: 5,
    # sent messages
    0xe4: 5, 0x1fa: 8, 0x200: 6, 0x30c: 8, 0x33d: 5, 0x35e: 8, 0x39f: 8,
  }],
  HONDA.CRV: [{
    57L: 3, 145L: 8, 316L: 8, 340L: 8, 342L: 6, 344L: 8, 380L: 8, 398L: 3, 399L: 6, 401L: 8, 420L: 8, 422L: 8, 426L: 8, 432L: 7, 464L: 8, 474L: 5, 476L: 4, 487L: 4, 490L: 8, 493L: 3, 507L: 1, 542L: 7, 545L: 4, 597L: 8, 660L: 8, 661L: 4, 773L: 7, 777L: 8, 800L: 8, 804L: 8, 808L: 8, 882L: 2, 884L: 7, 888L: 8, 891L: 8, 892L: 8, 923L: 2, 929L: 8, 983L: 8, 985L: 3, 1024L: 5, 1027L: 5, 1029L: 8, 1033L: 5, 1036L: 8, 1039L: 8, 1057L: 5, 1064L: 7, 1108L: 8, 1125L: 8, 1296L: 8, 1365L: 5, 1424L: 5, 1600L: 5, 1601L: 8,
    # sent messages
    0x194: 4, 0x1fa: 8, 0x30c: 8, 0x33d: 5,
  }],
  HONDA.ODYSSEY: [{
    57L: 3, 148L: 8, 228L: 5, 229L: 4, 316L: 8, 342L: 6, 344L: 8, 380L: 8, 399L: 7, 411L: 5, 419L: 8, 420L: 8, 427L: 3, 432L: 7, 450L: 8, 463L: 8, 464L: 8, 476L: 4, 490L: 8, 506L: 8, 542L: 7, 545L: 6, 597L: 8, 662L: 4, 773L: 7, 777L: 8, 780L: 8, 795L: 8, 800L: 8, 804L: 8, 806L: 8, 808L: 8, 817L: 4, 819L: 7, 821L: 5, 825L: 4, 829L: 5, 837L: 5, 856L: 7, 862L: 8, 871L: 8, 881L: 8, 882L: 4, 884L: 8, 891L: 8, 892L: 8, 905L: 8, 923L: 2, 927L: 8, 929L: 8, 963L: 8, 965L: 8, 966L: 8, 967L: 8, 983L: 8, 985L: 3, 1029L: 8, 1036L: 8, 1052L: 8, 1064L: 7, 1088L: 8, 1089L: 8, 1092L: 1, 1108L: 8, 1110L: 8, 1125L: 8, 1296L: 8, 1302L: 8, 1600L: 5, 1601L: 8, 1612L: 5, 1613L: 5, 1614L: 5, 1615L: 8, 1616L: 5, 1619L: 5, 1623L: 5, 1668L: 5
  },
  # Odyssey Elite
  {
    57L: 3, 148L: 8, 228L: 5, 229L: 4, 304L: 8, 342L: 6, 344L: 8, 380L: 8, 399L: 7, 411L: 5, 419L: 8, 420L: 8, 427L: 3, 432L: 7, 440L: 8, 450L: 8, 463L: 8, 464L: 8, 476L: 4, 490L: 8, 506L: 8, 507L: 1, 542L: 7, 545L: 6, 597L: 8, 662L: 4, 773L: 7, 777L: 8, 780L: 8, 795L: 8, 800L: 8, 804L: 8, 806L: 8, 808L: 8, 817L: 4, 819L: 7, 821L: 5, 825L: 4, 829L: 5, 837L: 5, 856L: 7, 862L: 8, 871L: 8, 881L: 8, 882L: 4, 884L: 8, 891L: 8, 892L: 8, 905L: 8, 923L: 2, 927L: 8, 929L: 8, 963L: 8, 965L: 8, 966L: 8, 967L: 8, 983L: 8, 985L: 3, 1029L: 8, 1036L: 8, 1052L: 8, 1064L: 7, 1088L: 8, 1089L: 8, 1092L: 1, 1108L: 8, 1110L: 8, 1125L: 8, 1296L: 8, 1302L: 8, 1600L: 5, 1601L: 8, 1612L: 5, 1613L: 5, 1614L: 5, 1616L: 5, 1619L: 5, 1623L: 5, 1668L: 5
  }],
  HONDA.PILOT: [{
    1600L: 5, 1027L: 5, 1668L: 5, 1029L: 8, 1601L: 8, 777L: 8, 891L: 8, 1036L: 8, 399L: 7, 1424L: 5, 145L: 8, 660L: 8, 985L: 3, 1616L: 5, 538L: 3, 795L: 8, 542L: 7, 773L: 7, 800L: 8, 545L: 5, 546L: 3, 419L: 8, 420L: 8, 422L: 8, 1064L: 7, 425L: 8, 426L: 8, 427L: 3, 432L: 7, 819L: 7, 308L: 5, 821L: 5, 57L: 3, 965L: 8, 316L: 8, 829L: 5, 1088L: 8, 1089L: 8, 963L: 8, 837L: 5, 966L: 8, 929L: 8, 780L: 8, 923L: 2, 1613L: 5, 334L: 8, 463L: 8, 464L: 8, 1618L: 5, 1108L: 8, 597L: 8, 342L: 6, 983L: 8, 856L: 7, 804L: 8, 1612L: 5, 476L: 4, 1125L: 8, 344L: 8, 1296L: 8, 379L: 8, 228L: 5, 229L: 4, 871L: 8, 892L: 8, 490L: 8, 808L: 8, 882L: 2, 884L: 7, 967L: 8, 506L: 8, 507L: 1, 380L: 8,
  }],
  TOYOTA.RAV4: [{
    36L: 8, 37L: 8, 170L: 8, 180L: 8, 186L: 4, 426L: 6, 452L: 8, 464L: 8, 466L: 8, 467L: 8, 547L: 8, 548L: 8, 552L: 4, 562L: 4, 608L: 8, 610L: 5, 643L: 7, 705L: 8, 725L: 2, 740L: 5, 800L: 8, 835L: 8, 836L: 8, 849L: 4, 869L: 7, 870L: 7, 871L: 2, 896L: 8, 897L: 8, 900L: 6, 902L: 6, 905L: 8, 911L: 8, 916L: 3, 918L: 7, 921L: 8, 933L: 8, 944L: 8, 945L: 8, 951L: 8, 955L: 4, 956L: 8, 979L: 2, 998L: 5, 999L: 7, 1000L: 8, 1001L: 8, 1005L: 2, 1008L: 2, 1014L: 8, 1017L: 8, 1041L: 8, 1042L: 8, 1043L: 8, 1044L: 8, 1056L: 8, 1059L: 1, 1114L: 8, 1161L: 8, 1162L: 8, 1163L: 8, 1176L: 8, 1177L: 8, 1178L: 8, 1179L: 8, 1180L: 8, 1181L: 8, 1190L: 8, 1191L: 8, 1192L: 8, 1196L: 8, 1227L: 8, 1228L: 8, 1235L: 8, 1237L: 8, 1263L: 8, 1264L: 8, 1279L: 8, 1408L: 8, 1409L: 8, 1410L: 8, 1552L: 8, 1553L: 8, 1554L: 8, 1555L: 8, 1556L: 8, 1557L: 8, 1561L: 8, 1562L: 8, 1568L: 8, 1569L: 8, 1570L: 8, 1571L: 8, 1572L: 8, 1584L: 8, 1589L: 8, 1592L: 8, 1593L: 8, 1595L: 8, 1596L: 8, 1597L: 8, 1600L: 8, 1656L: 8, 1664L: 8, 1728L: 8, 1745L: 8, 1779L: 8, 1904L: 8, 1912L: 8, 1990L: 8, 1998L: 8
  }],
  TOYOTA.RAV4H: [{
    36L: 8, 37L: 8, 170L: 8, 180L: 8, 186L: 4, 296L: 8, 426L: 6, 452L: 8, 464L: 8, 466L: 8, 467L: 8, 547L: 8, 548L: 8, 550L: 8, 552L: 4, 560L: 7, 562L: 4, 581L: 5, 608L: 8, 610L: 5, 643L: 7, 705L: 8, 713L: 8, 725L: 2, 740L: 5, 800L: 8, 835L: 8, 836L: 8, 849L: 4, 869L: 7, 870L: 7, 871L: 2, 896L: 8, 897L: 8, 900L: 6, 902L: 6, 905L: 8, 911L: 8, 916L: 3, 918L: 7, 921L: 8, 933L: 8, 944L: 8, 945L: 8, 950L: 8, 951L: 8, 953L: 3, 955L: 8, 956L: 8, 979L: 2, 998L: 5, 999L: 7, 1000L: 8, 1001L: 8, 1005L: 2, 1008L: 2, 1014L: 8, 1017L: 8, 1041L: 8, 1042L: 8, 1043L: 8, 1044L: 8, 1056L: 8, 1059L: 1, 1114L: 8, 1161L: 8, 1162L: 8, 1163L: 8, 1176L: 8, 1177L: 8, 1178L: 8, 1179L: 8, 1180L: 8, 1181L: 8, 1184L: 8, 1185L: 8, 1186L: 8, 1190L: 8, 1191L: 8, 1192L: 8, 1196L: 8, 1197L: 8, 1198L: 8, 1199L: 8, 1212L: 8, 1227L: 8, 1228L: 8, 1232L: 8, 1235L: 8, 1237L: 8, 1263L: 8, 1264L: 8, 1279L: 8, 1408L: 8, 1409L: 8, 1410L: 8, 1552L: 8, 1553L: 8, 1554L: 8, 1555L: 8, 1556L: 8, 1557L: 8, 1561L: 8, 1562L: 8, 1568L: 8, 1569L: 8, 1570L: 8, 1571L: 8, 1572L: 8, 1584L: 8, 1589L: 8, 1592L: 8, 1593L: 8, 1595L: 8, 1596L: 8, 1597L: 8, 1600L: 8, 1656L: 8, 1664L: 8, 1728L: 8, 1745L: 8, 1779L: 8, 1904L: 8, 1912L: 8, 1990L: 8, 1998L: 8
 }],
  TOYOTA.PRIUS: [{
    36L: 8, 37L: 8, 166L: 8, 170L: 8, 180L: 8, 295L: 8, 296L: 8, 426L: 6, 452L: 8, 466L: 8, 467L: 8, 550L: 8, 552L: 4, 560L: 7, 562L: 6, 581L: 5, 608L: 8, 610L: 8, 614L: 8, 643L: 7, 658L: 8, 713L: 8, 740L: 5, 742L: 8, 743L: 8, 800L: 8, 810L: 2, 814L: 8, 829L: 2, 830L: 7, 835L: 8, 836L: 8, 863L: 8, 869L: 7, 870L: 7, 871L: 2, 898L: 8, 900L: 6, 902L: 6, 905L: 8, 918L: 8, 921L: 8, 933L: 8, 944L: 8, 945L: 8, 950L: 8, 951L: 8, 953L: 8, 955L: 8, 956L: 8, 971L: 7, 975L: 5, 993L: 8, 998L: 5, 999L: 7, 1000L: 8, 1001L: 8, 1014L: 8, 1017L: 8, 1020L: 8, 1041L: 8, 1042L: 8, 1044L: 8, 1056L: 8, 1057L: 8, 1059L: 1, 1071L: 8, 1077L: 8, 1082L: 8, 1083L: 8, 1084L: 8, 1085L: 8, 1086L: 8, 1114L: 8, 1132L: 8, 1161L: 8, 1162L: 8, 1163L: 8, 1175L: 8, 1227L: 8, 1228L: 8, 1235L: 8, 1237L: 8, 1279L: 8, 1552L: 8, 1553L: 8, 1556L: 8, 1557L: 8, 1568L: 8, 1570L: 8, 1571L: 8, 1572L: 8, 1595L: 8, 1777L: 8, 1779L: 8, 1904L: 8, 1912L: 8, 1990L: 8, 1998L: 8
  },
  # Prius Prime
  {
    36L: 8, 37L: 8, 166L: 8, 170L: 8, 180L: 8, 295L: 8, 296L: 8, 426L: 6, 452L: 8, 466L: 8, 467L: 8, 550L: 8, 552L: 4, 560L: 7, 562L: 6, 581L: 5, 608L: 8, 610L: 8, 614L: 8, 643L: 7, 658L: 8, 713L: 8, 740L: 5, 742L: 8, 743L: 8, 800L: 8, 810L: 2, 814L: 8, 824L: 2, 829L: 2, 830L: 7, 835L: 8, 836L: 8, 863L: 8, 869L: 7, 870L: 7, 871L: 2,898L: 8, 900L: 6, 902L: 6, 905L: 8, 913L: 8, 918L: 8, 921L: 8, 933L: 8, 944L: 8, 945L: 8, 950L: 8, 951L: 8, 953L: 8, 955L: 8, 956L: 8, 971L: 7, 974L: 8, 975L: 5, 993L: 8, 998L: 5, 999L: 7, 1000L: 8, 1001L: 8, 1014L: 8, 1017L: 8, 1020L: 8, 1041L: 8, 1042L: 8, 1044L: 8, 1056L: 8, 1057L: 8, 1059L: 1, 1071L: 8, 1076L: 8, 1077L: 8, 1082L: 8, 1083L: 8, 1084L: 8, 1085L: 8, 1086L: 8, 1114L: 8, 1132L: 8, 1161L: 8, 1162L: 8, 1163L: 8, 1164L: 8, 1165L: 8, 1166L: 8, 1167L: 8, 1175L: 8, 1227L: 8, 1228L: 8, 1235L: 8, 1237L: 8, 1279L: 8, 1552L: 8, 1553L: 8, 1556L: 8, 1557L: 8, 1568L: 8, 1570L: 8, 1571L: 8, 1572L: 8, 1595L: 8, 1777L: 8, 1779L: 8, 1904L: 8, 1912L: 8, 1990L: 8, 1998L: 8
  },
  # Taiwanese Prius Prime
  {
    36L: 8, 37L: 8, 166L: 8, 170L: 8, 180L: 8, 295L: 8, 296L: 8, 426L: 6, 452L: 8, 466L: 8, 467L: 8, 550L: 8, 552L: 4, 560L: 7, 562L: 6, 581L: 5, 608L: 8, 610L: 8, 614L: 8, 643L: 7, 658L: 8, 713L: 8, 740L: 5, 742L: 8, 743L: 8, 800L: 8, 810L: 2, 814L: 8, 824L: 2, 829L: 2, 830L: 7, 835L: 8, 836L: 8, 845L: 5, 863L: 8, 869L: 7, 870L: 7, 871L: 2,898L: 8, 900L: 6, 902L: 6, 905L: 8, 913L: 8, 918L: 8, 921L: 8, 933L: 8, 944L: 8, 945L: 8, 950L: 8, 951L: 8, 953L: 8, 955L: 8, 956L: 8, 971L: 7, 974L: 8, 975L: 5, 993L: 8, 998L: 5, 999L: 7, 1000L: 8, 1001L: 8, 1005L: 2, 1014L: 8, 1017L: 8, 1020L: 8, 1041L: 8, 1042L: 8, 1044L: 8, 1056L: 8, 1057L: 8, 1059L: 1, 1071L: 8, 1076L: 8, 1077L: 8, 1082L: 8, 1083L: 8, 1084L: 8, 1085L: 8, 1086L: 8, 1114L: 8, 1132L: 8, 1161L: 8, 1162L: 8, 1163L: 8, 1164L: 8, 1165L: 8, 1166L: 8, 1167L: 8, 1175L: 8, 1227L: 8, 1228L: 8, 1235L: 8, 1237L: 8, 1264L: 8, 1279L: 8, 1552L: 8, 1553L: 8, 1556L: 8, 1557L: 8, 1568L: 8, 1570L: 8, 1571L: 8, 1572L: 8, 1595L: 8, 1777L: 8, 1779L: 8, 1904L: 8, 1912L: 8, 1990L: 8, 1998L: 8
  }],
  TOYOTA.COROLLA: [{
    36: 8, 37: 8, 170: 8, 180: 8, 186: 4, 426: 6, 452: 8, 464: 8, 466: 8, 467: 8, 547: 8, 548: 8, 552: 4, 608: 8, 610: 5, 643: 7, 705: 8, 740: 5, 800: 8, 835: 8, 836: 8, 849: 4, 869: 7, 870: 7, 871: 2, 896: 8, 897: 8, 900: 6, 902: 6, 905: 8, 911: 8, 916: 2, 921: 8, 933: 8, 944: 8, 945: 8, 951: 8, 955: 4, 956: 8, 979: 2, 992: 8, 998: 5, 999: 7, 1000: 8, 1001: 8, 1017: 8, 1041: 8, 1042: 8, 1043: 8, 1044: 8, 1056: 8, 1059: 1, 1114: 8, 1161: 8, 1162: 8, 1163: 8, 1196: 8, 1227: 8, 1235: 8, 1279: 8, 1552: 8, 1553: 8, 1556: 8, 1557: 8, 1561: 8, 1562: 8, 1568: 8, 1569: 8, 1570: 8, 1571: 8, 1572: 8, 1584: 8, 1589: 8, 1592: 8, 1596: 8, 1597: 8, 1600: 8, 1664: 8, 1728: 8, 1779: 8, 1904: 8, 1912: 8, 1990: 8, 1998: 8
  }],
  TOYOTA.LEXUS_RXH: [{
    36: 8, 37: 8, 166: 8, 170: 8, 180: 8, 295: 8, 296: 8, 426: 6, 452: 8, 466: 8, 467: 8, 550: 8, 552: 4, 560: 7, 562: 6, 581: 5, 608: 8, 610: 5, 643: 7, 658: 8, 713: 8, 740: 5, 742: 8, 743: 8, 800: 8, 810: 2, 812: 3, 814: 8, 830: 7, 835: 8, 836: 8, 845: 5, 863: 8, 869: 7, 870: 7, 871: 2, 898: 8, 900: 6, 902: 6, 905: 8, 913: 8, 918: 8, 921: 8, 933: 8, 944: 8, 945: 8, 950: 8, 951: 8, 953: 8, 955: 8, 956: 8, 971: 7, 975: 6, 993: 8, 998: 5, 999: 7, 1000: 8, 1001: 8, 1005: 2, 1014: 8, 1017: 8, 1020: 8, 1041: 8, 1042: 8, 1044: 8, 1056: 8, 1059: 1, 1063: 8, 1071: 8, 1077: 8, 1082: 8, 1114: 8, 1161: 8, 1162: 8, 1163: 8, 1164: 8, 1165: 8, 1166: 8, 1167: 8, 1227: 8, 1228: 8, 1235: 8, 1237: 8, 1264: 8, 1279: 8, 1552: 8, 1553: 8, 1556: 8, 1557: 8, 1568: 8, 1570: 8, 1571: 8, 1572: 8, 1575: 8, 1595: 8, 1777: 8, 1779: 8, 1808: 8, 1810: 8, 1816: 8, 1818: 8, 1840: 8, 1848: 8, 1904: 8, 1912: 8, 1940: 8, 1941: 8, 1948: 8, 1949: 8, 1952: 8, 1956: 8, 1960: 8, 1964: 8, 1986: 8, 1990: 8, 1994: 8, 1998: 8, 2004: 8, 2012: 8
  }],
  GM.VOLT: [{
    # Powertrain CAN
    170L: 8, 171L: 8, 189L: 7, 190L: 6, 193L: 8, 197L: 8, 199L: 4, 201L: 8, 209L: 7, 211L: 2, 241L: 6, 288L: 5, 289L: 8, 298L: 8, 304L: 1, 308L: 4, 309L: 8, 311L: 8, 313L: 8, 320L: 3, 328L: 1, 352L: 5, 381L: 6, 384L: 4, 386L: 8, 388L: 8, 389L: 2, 390L: 7, 417L: 7, 419L: 1, 426L: 7, 451L: 8, 452L: 8, 453L: 6, 454L: 8, 456L: 8, 479L: 3, 481L: 7, 485L: 8, 489L: 8, 493L: 8, 495L: 4, 497L: 8, 499L: 3, 500L: 6, 501L: 8, 508L: 8, 528L: 4, 532L: 6, 546L: 7, 550L: 8, 554L: 3, 558L: 8, 560L: 8, 562L: 8, 563L: 5, 564L: 5, 565L: 5, 566L: 5, 567L: 3, 568L: 1, 573L: 1, 647L: 3, 707L: 8, 711L: 6, 715L: 8, 717L: 5, 761L: 7, 810L: 8, 840L: 5, 842L: 5, 844L: 8, 866L: 4, 869L: 4, 880L: 6, 961L: 8, 969L: 8, 977L: 8, 979L: 7, 988L: 6, 989L: 8, 995L: 7, 1001L: 8, 1005L: 6, 1009L: 8, 1017L: 8, 1019L: 2, 1020L: 8, 1033L: 7, 1034L: 7, 1105L: 6, 1187L: 4, 1217L: 8, 1221L: 5, 1223L: 3, 1225L: 7, 1227L: 4, 1233L: 8, 1249L: 8, 1257L: 6, 1265L: 8, 1267L: 1, 1273L: 3, 1275L: 3, 1280L: 4, 1296L: 4, 1300L: 8, 1322L: 6, 1323L: 4, 1328L: 4, 1417L: 8, 1905L: 7, 1906L: 7, 1907L: 7, 1910L: 7, 1912L: 7, 1922L: 7, 1927L: 7, 1928L: 7, 1930L: 7,

    # Object detection CAN, minus overlaps that conflict with powertrain forwarding:
    # 309L: 1, 1296L: 7, 1322L: 7, 1323L: 7, 1328L: 8
    161L: 7, 262L: 5, 768L: 8, 771L: 2, 774L: 8, 776L: 7, 784L: 2, 848L: 8, 849L: 8, 850L: 8, 851L: 8, 852L: 8, 853L: 8, 854L: 3, 1033L: 7, 1034L: 7, 1056L: 6, 1057L: 8, 1058L: 8, 1059L: 8, 1060L: 8, 1061L: 8, 1062L: 8, 1063L: 8, 1064L: 8, 1065L: 8, 1066L: 8, 1067L: 8, 1068L: 8, 1088L: 8, 1089L: 8, 1090L: 8, 1091L: 8, 1092L: 8, 1093L: 8, 1094L: 8, 1095L: 8, 1096L: 8, 1097L: 8, 1098L: 8, 1099L: 8, 1100L: 8, 1120L: 8, 1121L: 8, 1122L: 8, 1123L: 8, 1124L: 8, 1125L: 8, 1126L: 8, 1127L: 8, 1128L: 8, 1129L: 8, 1130L: 8, 1131L: 8, 1132L: 8, 1133L: 8, 1134L: 8, 1135L: 8, 1136L: 8, 1137L: 8, 1138L: 8, 1139L: 8, 1140L: 8, 1141L: 8, 1142L: 8, 1143L: 8, 1146L: 8, 1147L: 8, 1148L: 8, 1149L: 8, 1150L: 8, 1151L: 8, 1297L: 8, 1298L: 8, 1299L: 8, 1300L: 8, 1301L: 8, 1302L: 8, 1303L: 8, 1304L: 8, 1305L: 8, 1306L: 8, 1307L: 8, 1308L: 8, 1309L: 8, 1310L: 8, 1311L: 8, 1313L: 7, 1314L: 7, 1315L: 7, 1316L: 7, 1317L: 7, 1318L: 7, 1319L: 7, 1320L: 7, 1321L: 7, 1324L: 7, 1325L: 7, 1326L: 7, 1327L: 7, 1331L: 8, 1335L: 8, 1338L: 8, 1344L: 8, 1362L: 8, 1408L: 8, 1409L: 8, 1410L: 6, 1412L: 8, 1413L: 5, 1414L: 7, 1857L: 8, 1859L: 8, 1920L: 7,

    # Chassis CAN
    # 192L: 5, 193L: 8, 197L: 8, 201L: 6, 289L: 1, 290L: 1, 298L: 2, 304L: 8, 320L: 8, 368L: 8, 381L: 2, 384L: 8, 386L: 5, 388L: 6, 458L: 8, 485L: 8, 489L: 5, 501L: 3, 508L: 8, 512L: 3, 530L: 8, 532L: 7, 537L: 5, 539L: 8, 542L: 7, 560L: 6, 562L: 4, 565L: 8, 568L: 2, 789L: 5, 800L: 6, 801L: 5, 805L: 8, 821L: 4, 823L: 7, 832L: 8, 840L: 6, 842L: 6, 869L: 4, 1001L: 5, 1003L: 5, 1249L: 8, 1300L: 8,

    # Low-speed GMLAN, sender ECU dropped for extended
    # 1568L: 8, 1569L: 8, 1572L: 8, 1580L: 8, 203997184L: 8, 204464128L: 1, 207814656L: 1, 209264640L: 5, 209715200L: 6, 270581760L: 5, 270598144L: 8, 270663680L: 8, 270704640L: 8, 270712832L: 6, 270721024L: 8, 270729216L: 8, 270794752L: 8, 270802944L: 1, 270811136L: 1, 270827520L: 7, 270860288L: 2, 270942208L: 8, 270974976L: 5, 271032320L: 8, 271220736L: 6, 271228928L: 8, 271237120L: 8, 271319040L: 5, 271343616L: 6, 271360000L: 8, 271368192L: 8, 271376384L: 8, 271384576L: 8, 271450112L: 8, 271597568L: 3, 271605760L: 3, 271613952L: 3, 271728640L: 6, 272154624L: 5, 272384000L: 1, 272433152L: 1, 272457728L: 7, 272629760L: 5, 272670720L: 1, 272924672L: 4, 273047552L: 5, 273080320L: 4, 273129472L: 1, 274259968L: 4, 274907136L: 5, 275480576L: 8, 275513344L: 5, 275521536L: 1, 275578880L: 2, 275595264L: 3, 275644416L: 2, 275791872L: 4, 275988480L: 6, 276127744L: 1, 276135936L: 3, 276283392L: 4, 276299776L: 8, 276316160L: 5, 276332544L: 6, 276848640L: 5, 276865024L: 7, 276905984L: 4, 277741568L: 6, 279764992L: 8, 279797760L: 8, 283918336L: 8, 283934720L: 8, 335536128L: 0,
  }],
}

# support additional internal only fingerprints
try:
  from common.fingerprints_internal import add_additional_fingerprints
  add_additional_fingerprints(_FINGERPRINTS)
except ImportError:
  pass


def is_valid_for_fingerprint(msg, car_fingerprint):
  adr = msg.address
  return msg.src != 0 or (adr in car_fingerprint and car_fingerprint[adr] == len(msg.dat))


def eliminate_incompatible_cars(msg, candidate_cars):
  """Removes cars that could not have sent msg.

     Inputs:
      msg: A cereal/log CanData message from the car.
      candidate_cars: A list of cars to consider.

     Returns:
      A list containing the subset of candidate_cars that could have sent msg.
  """
  compatible_cars = []
  for car_name in candidate_cars:
    car_fingerprints = _FINGERPRINTS[car_name]

    for fingerprint in car_fingerprints:
      fingerprint.update(_DEBUG_ADDRESS)  # add alien debug address

      if is_valid_for_fingerprint(msg, fingerprint):
        compatible_cars.append(car_name)
        break

  return compatible_cars


def all_known_cars():
  """Returns a list of all known car strings."""
  return _FINGERPRINTS.keys()

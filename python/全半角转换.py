# -*- coding: utf-8 -*-
#!/bin/python3
'''
全角/半角 转换工具
转换表如下,不含日/韩文:
0x20    "　"     U+3000  " "     U+0020
0x21    ！   U+FF01  !   U+0021
0x22    ＂   U+FF02  "   U+0022
0x23    ＃   U+FF03  #   U+0023
0x24    ＄   U+FF04  $   U+0024
0x25    ％   U+FF05  %   U+0025
0x26    ＆   U+FF06  &   U+0026
0x27    ＇   U+FF07  '   U+0027
0x28    （   U+FF08  (   U+0028
0x29    ）   U+FF09  )   U+0029
0x2A    ＊   U+FF0A  *   U+002A
0x2B    ＋   U+FF0B  +   U+002B
0x2C    ，   U+FF0C  ,   U+002C
0x2D    －   U+FF0D  -   U+002D
0x2E    ．   U+FF0E  .   U+002E
0x2F    ／   U+FF0F  /   U+002F
0x30    ０   U+FF10  0   U+0030
0x31    １   U+FF11  1   U+0031
0x32    ２   U+FF12  2   U+0032
0x33    ３   U+FF13  3   U+0033
0x34    ４   U+FF14  4   U+0034
0x35    ５   U+FF15  5   U+0035
0x36    ６   U+FF16  6   U+0036
0x37    ７   U+FF17  7   U+0037
0x38    ８   U+FF18  8   U+0038
0x39    ９   U+FF19  9   U+0039
0x3A    ：   U+FF1A  :   U+003A
0x3B    ；   U+FF1B  ;   U+003B
0x3C    ＜   U+FF1C  <   U+003C
0x3D    ＝   U+FF1D  =   U+003D
0x3E    ＞   U+FF1E  >   U+003E
0x3F    ？   U+FF1F  ?   U+003F
0x40    ＠   U+FF20  @   U+0040
0x41    Ａ   U+FF21  A   U+0041
0x42    Ｂ   U+FF22  B   U+0042
0x43    Ｃ   U+FF23  C   U+0043
0x44    Ｄ   U+FF24  D   U+0044
0x45    Ｅ   U+FF25  E   U+0045
0x46    Ｆ   U+FF26  F   U+0046
0x47    Ｇ   U+FF27  G   U+0047
0x48    Ｈ   U+FF28  H   U+0048
0x49    Ｉ   U+FF29  I   U+0049
0x4A    Ｊ   U+FF2A  J   U+004A
0x4B    Ｋ   U+FF2B  K   U+004B
0x4C    Ｌ   U+FF2C  L   U+004C
0x4D    Ｍ   U+FF2D  M   U+004D
0x4E    Ｎ   U+FF2E  N   U+004E
0x4F    Ｏ   U+FF2F  O   U+004F
0x50    Ｐ   U+FF30  P   U+0050
0x51    Ｑ   U+FF31  Q   U+0051
0x52    Ｒ   U+FF32  R   U+0052
0x53    Ｓ   U+FF33  S   U+0053
0x54    Ｔ   U+FF34  T   U+0054
0x55    Ｕ   U+FF35  U   U+0055
0x56    Ｖ   U+FF36  V   U+0056
0x57    Ｗ   U+FF37  W   U+0057
0x58    Ｘ   U+FF38  X   U+0058
0x59    Ｙ   U+FF39  Y   U+0059
0x5A    Ｚ   U+FF3A  Z   U+005A
0x5B    ［   U+FF3B  [   U+005B
0x5C    ＼   U+FF3C  \   U+005C
0x5D    ］   U+FF3D  ]   U+005D
0x5E    ＾   U+FF3E  ^   U+005E
0x5F    ＿   U+FF3F  _   U+005F
0x60    ｀   U+FF40  `   U+0060
0x61    ａ   U+FF41  a   U+0061
0x62    ｂ   U+FF42  b   U+0062
0x63    ｃ   U+FF43  c   U+0063
0x64    ｄ   U+FF44  d   U+0064
0x65    ｅ   U+FF45  e   U+0065
0x66    ｆ   U+FF46  f   U+0066
0x67    ｇ   U+FF47  g   U+0067
0x68    ｈ   U+FF48  h   U+0068
0x69    ｉ   U+FF49  i   U+0069
0x6A    ｊ   U+FF4A  j   U+006A
0x6B    ｋ   U+FF4B  k   U+006B
0x6C    ｌ   U+FF4C  l   U+006C
0x6D    ｍ   U+FF4D  m   U+006D
0x6E    ｎ   U+FF4E  n   U+006E
0x6F    ｏ   U+FF4F  o   U+006F
0x70    ｐ   U+FF50  p   U+0070
0x71    ｑ   U+FF51  q   U+0071
0x72    ｒ   U+FF52  r   U+0072
0x73    ｓ   U+FF53  s   U+0073
0x74    ｔ   U+FF54  t   U+0074
0x75    ｕ   U+FF55  u   U+0075
0x76    ｖ   U+FF56  v   U+0076
0x77    ｗ   U+FF57  w   U+0077
0x78    ｘ   U+FF58  x   U+0078
0x79    ｙ   U+FF59  y   U+0079
0x7A    ｚ   U+FF5A  z   U+007A
0x7B    ｛   U+FF5B  {   U+007B
0x7C    ｜   U+FF5C  |   U+007C
0x7D    ｝   U+FF5D  }   U+007D
0x7E    ～   U+FF5E  ~   U+007E

除空格外,其他都是对应差值.
'''
f2h_table_builder = {
    lambda: range(0xff01, 0xff5e + 1): lambda x: x - 0xfee0,
    lambda: range(0x3000, 0x3000 + 1): lambda x: 0x0020
}

h2f_table_builder = {
    lambda: range(0x0021, 0x007e + 1): lambda x: x + 0xfee0,
    #lambda: range(0x0020, 0x0020 + 1): lambda x: 0x3000
}


def build_convert_table(builder):
    table = {}
    for range_func, func in builder.items():
        range_list = range_func()
        for k in range_list:
            table[k] = func
    return table


def string_convert(f_string, table):
    ustring = f_string
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code in table:
            rstring += chr(table[inside_code](inside_code))
        else:
            rstring += chr(inside_code)
    return rstring


def main(f2h, file_string):
    table = build_convert_table(f2h_table_builder if f2h else h2f_table_builder)
    for line in open(file_string):
        print (string_convert(line.strip(), table))


if __name__ == '__main__':
    import sys
    file_string = sys.argv[2]
    f2h = True if sys.argv[1] == 'h' else False
    main(f2h, file_string)

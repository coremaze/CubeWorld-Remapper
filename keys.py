CWKeycodes = ['','','','','','','','','','','','','','','','','','','','','','','','','',
'',
'',
'',
'',
'',
'',
'',
'',
'BACKSPACE',
'TAB',
'',
'',
'',
'',
'',
'',
'SHIFT',
'CTRL',
'',
'PAUSE/BREAK',
'CAPSLOCK',
'',
'',
'',
'',
'',
'',
'ESCAPE',
'',
'',
'',
'',
'',
'PAGE UP',
'PAGE DOWN',
'END',
'HOME',
'LEFT ARROW',
'UP ARROW',
'RIGHT ARROW',
'DOWN ARROW',
'',
'',
'',
'',
'INSERT',
'DELETE',
'',
'0',
'1',
'2',
'3',
'4',
'5',
'6',
'7',
'8',
'9',
'',
'',
'',
'',
'',
'',
'',
'A',
'B',
'C',
'D',
'E',
'F',
'G',
'H',
'I',
'J',
'K',
'L',
'M',
'N',
'O',
'P',
'Q',
'R',
'S',
'T',
'U',
'V',
'W',
'X',
'Y',
'Z',
'LEFT WINDOWS KEY',
'RIGHT WINDOWS KEY',
'',
'',
'',
'NUMPAD 0',
'NUMPAD 1',
'NUMPAD 2',
'NUMPAD 3',
'NUMPAD 4',
'NUMPAD 5',
'NUMPAD 6',
'NUMPAD 7',
'NUMPAD 8',
'NUMPAD 9',
'NUMPAD *',
'NUMPAD +',
'',
'NUMPAD -',
'NUMPAD .',
'NUMPAD /',
'F1',
'F2',
'F3',
'F4',
'F5',
'F6',
'F7',
'F8',
'F9',
'F10',
'F11',
'F12',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'NUMLOCK',
'SCROLL LOCK',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
';',
'=',
',',
'-',
'.',
'/',
'`',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'',
'[',
'\\', #fuck
']',
"'", #lmao
'',
'',
'',
'',
'',
'',
'',
'',
'',
'M1',
'M2',
'M3'
]

CWSwitchKeyCodes = [
'TAB',#9  
'',#10 
'',#11 
'',#12 
'',#13 
'',#14 
'',#15 
'SHIFT',#16 
'CTRL',#17 
'',#18 
'PAUSE/BREAK',#19 
'CAPSLOCK',#20 
'',#21 
'',#22 
'',#23 
'',#24 
'',#25 
'',#26 
'ESCAPE',#27 
'',#28 
'',#29 
'',#30 
'',#31 
'SPACE',#32 
'PAGE UP',#33 
'PAGE DOWN',#34 
'END',#35 
'HOME',#36 
'LEFT ARROW',#37 
'UP ARROW',#38 
'RIGHT ARROW',#39 
'DOWN ARROW',#40 
'',#41 
'',#42 
'',#43 
'',#44 
'INSERT',#45 
'DELETE',#46 
'0',#47 
'1',#48 
'2',#49 
'3',#50 
'4',#51 
'5',#52 
'6',#53 
'7',#54 
'8',#55 
'9',#56 
'',#57 
'',#58 
'',#59 
'',#60 
'',#61 
'',#62 
'',#63 
'',#64 
'A',#65 
'B',#66 
'C',#67 
'D',#68 
'E',#69 
'F',#70 
'G',#71 
'H',#72 
'I',#73 
'J',#74 
'K',#75 
'L',#76 
'M',#77 
'N',#78 
'O',#79 
'P',#80 
'Q',#81 
'R',#82 
'S',#83 
'T',#84 
'U',#85 
'V',#86 
'W',#87 
'X',#88 
'Y',#89 
'Z',#90 
'LEFT WINDOWS KEY',#91 
'RIGHT WINDOWS KEY',#92 
'SELECT',#93 - this key doesn't really exist anymore... 
'',#94 
'',#95 
'NUMPAD 0',#96 
'NUMPAD 1',#97 
'NUMPAD 2',#98 
'NUMPAD 3',#99 
'NUMPAD 4',#100
'NUMPAD 5',#101
'NUMPAD 6',#102
'NUMPAD 7',#103
'NUMPAD 8',#104
'NUMPAD 9',#105
'NUMPAD *',#106
'NUMPAD +',#107
'',#108
'NUMPAD -',#109
'NUMPAD .',#110
'NUMPAD /',#111
'F1',#112
'F2',#113
'F3',#114
'F4',#115
'F5',#116
'F6',#117
'F7',#118
'F8',#119
'F9',#120
'F10',#121
'F11',#122
'F12',#123
''#124
]

hotKeyLocations = [[0xA629A],#w
                   [0xa6aa4],#a
                   [0xA6678],#s
                   [0xA69D0],#d
                   [0xA808C, 0xA81A2],#Spacebar
                   [0x97705, 0x9771A, 0x98260, 0x9A8D5, 0x91C0A], #Shift
                   [0x977F7], #ctrl
                   [0x969C3, 0x9A99D],#e
                   [0x9676E, 0x9A995],#r
                   [0x91839],#1
                   [0x918F7],#2
                   [0x919B5],#3
                   [0x96AE9, 0x9A9A5],#t
                   [0x91A73, 0x914B0, 0x9153D],#q
                   [0x95A31, 0x7E10F, 0x916BD, 0x9B3F4, 0x9B37E, 0x95ACB],#M1
                   [0x9B6B1, 0x9177B, 0x9B3CA],#M2 #Fix
                   [0x7E1E6, 0xA60D8],#M3
                   [0x9A9C0, 0x9A9FD]#Teleport to city
                   ]

def GetKeyCode(key, switch):
    
    if key == '':#User didn't press a key
        return 0 #All of those are invalid or unknown.
                 #CW's keycode structure seems irregular.
    if switch:
        arr = CWSwitchKeyCodes
    else:
        arr = CWKeycodes
    
    #Convert to caps
    key = key.upper()
    
    for i in range(0, len(arr)):
        if arr[i] == key:
            return i
    #Key not found
    return 0


        


    

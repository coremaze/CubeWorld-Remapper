from keys import *

def main():
    cubeName = input("Path to Cube.exe: ")
    try:
        hCube = open(cubeName, 'rb')
        cCube = hCube.read()
    except:
        print("Can't open %s" % cubeName)
        return
    
    cCube = [x for x in cCube]
    cCube[0x7DB5B] = 0x73 #Extend indirect switch table
    cCube[0x7DDC4:0x7DDD0] = [0xB]*12 #Set new cases to default

    print('''Select action to remap:
        1) Forward (W)
        2) Left (A)
        3) Backward (S)
        4) Right (D)
        5) Jump (Spacebar)
        6) Walk, Free Aim (Shift)
        7) Climb (Ctrl)
        
        8) Pick Up (E)
        9) Interact (R)

        10) Use Ability 1 (1)
        11) Use Ability 2 (2)
        12) Use Ability 3 (3)

        13) Call Pet (T)
        14) Use Quick Item (Q)

        15) Normal Attack (M1)
        16) Special Attack (M2)
        17) Dodge/Zoon (M3)

        18) Teleport to City (?)

        19) Select Quick Item (TAB)
        20) Menu (ESCAPE)
        21) Inventory (B, I)
        22) Crafting (C)
        23) Light (F)
        24) Special Item (G)
        25) Map (M)
        26) Options (O)
        27) Toggle HP Bars (V)
        28) Skills (X)
        29) Help (F1)
        [Enter] to exit''')
    while True:
        hotKey = input('Action # to remap: ')
        if hotKey == '':
            return
        try:
            hotKey = int(hotKey)
        except:
            print("You what")
        else:
            if hotKey not in range(1, 30):
                print("Invalid hotkey")
                
            else:
                #Valid hotkey
                if hotKey <= 18:
                    #A different process needs to occur for
                    #keys handled with a switch jump
                    keyName = input("Remap to: ")
                    keyCode = GetKeyCode(keyName, False)
                    #print(hex(int(keyCode)))
                    if keyCode == 0:
                        print("Invalid key.")
                    else:
                        #Valid remap key
                        for loc in hotKeyLocations[hotKey-1]:
                            cCube[loc] = keyCode
                            
                        hOut = open("Cube_remapped.exe", 'wb')
                        hOut.write(bytes(cCube))
                        hOut.close()

                else:
                    caseTableAddr = 0x7DD5C
                    caseTableEnd = 0x7DDD0
                    defaultCase = 0xB
                    
                    keyName = input("Remap to: ")
                    keyLoc = GetKeyCode(keyName, True)
                    if keyLoc == 0:
                        print('Invalid or unsupported key.')
                    else:
                        actionCase = hotKey - 19
                        for i in range(caseTableAddr, caseTableEnd):
                            if cCube[i] == actionCase:
                                cCube[i] = defaultCase #Unmap old keys
                                print('Unmapped')
                        if cCube[caseTableAddr+keyLoc] != defaultCase:
                            print('Overwriting an old mapping.')
                        cCube[caseTableAddr+keyLoc] = actionCase
                        
                        hOut = open("Cube_remapped.exe", 'wb')
                        hOut.write(bytes(cCube))
                        hOut.close()    
                    #Switch jump is at 0x7DB69
                    #Switch table is at 0x7DD5C                
                    
                
                

if __name__ == '__main__':
    main()

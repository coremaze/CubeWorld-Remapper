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
    while True:
        print('''Select key to remap:
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
        [Enter] to exit''')

        hotKey = input()
        if hotKey == '':
            return
        try:
            hotKey = int(hotKey)
        except:
            print("You what")
        else:
            if hotKey not in range(1, 19):
                print("Invalid hotkey")
                
            else:
                #Valid hotkey
                if hotKey <= 18:
                    #A different process needs to occur for
                    #keys handled with a switch jump
                    keyName = input("Remap to: ")
                    keyCode = GetKeyCode(keyName, False)
                    print(hex(int(keyCode)))
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
                    #TODO: switch jump keys
                    #Switch jump is at 0x7DB69
                    #Switch table is at 0x7DD5C
                    #Mappings affected:
                    #Use Quick Item (Tab)
                    #esc
                    #inventory (b, i)
                    #Crafting (c)
                    #Light (f)
                    #special item (g)
                    #map (m)
                    #options (o)
                    #toggle hp (v)
                    #skills (x)
                    #help (f1)                   
                    None
                
                

if __name__ == '__main__':
    main()

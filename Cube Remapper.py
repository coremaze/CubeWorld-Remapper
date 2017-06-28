from keys import *

def main():
    cubeName = input("Path to Cube.exe: ")
    try:
        hCube = open(cubeName, 'rb')
        cCube = hCube.read()
    except:
        print("Can't open %s" % cubeName)
    cCube = [x for x in cCube]
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
        [Enter] to exit''')

        hotKey = input()
        if hotKey == '':
            return
        try:
            hotKey = int(hotKey)
        except:
            print("You what")
        else:
            if hotKey not in range(1, 13):
                print("Invalid hotkey")
                
            else:
                #Valid hotkey
                keyName = input("Remap to: ")
                keyCode = GetKeyCode(keyName)
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
                
                

if __name__ == '__main__':
    main()

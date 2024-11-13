#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      LENOVO
#
# Created:     16-05-2024
# Copyright:   (c) LENOVO 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
move = input("you are standing on a place take left or right to proceed further. ")
if move == "left":
    print("good job")
    move = input("after moving right you are in front of a lake either you go for swim or wait? ")
    if move == "wait":
        print("you passed the second level")
        move = input("now you reached a home where you have three doors 'red','yellow','green' which one will you choose? ")
        if move == "yellow":
            print("you win the treasure")
        else:
            print("game over")
    else:
        print("game over")
else:
    print("game over")
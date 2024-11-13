#-------------------------------------------------------------------------------
# Name:
# Name:
# Purpose:
#
# Author:      LENOVO
# Created:     11-04-2024
# Copyright:   (c) LENOVO 2024
# Licence:     <your licence>
#---------------------------------------------

# LOVE CALCULATOR
print("Welcome To Love Calcuator.")
you = input ("write your name: ")
his_her = input("write your partner's name: " )
combine= you+his_her
lower = combine.lower()
t= lower.count("t")
r= lower.count("r")
u= lower.count("u")
e= lower.count("e")
true= t+r+u+e
#print(true)
l= lower.count("l")
o= lower.count("o")
v= lower.count("v")
e= lower.count("e")
love = l+o+v+e
#print(love)
love_score = str(true)+str(love)
print("your lovr score is ",love_score)

if int(love_score)<=30:
    print("you are not compatible for each other")
else:
    print("you are compatible for each other,BEST OF LUCK")
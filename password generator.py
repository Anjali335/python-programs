#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      LENOVO
#
# Created:     12-05-2024
# Copyright:   (c) LENOVO 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ["!","@","$","%","&"]
a = int(input("how many aplhabets would you like to insert \n"))
b = int(input("how many numbers would you like to insert \n"))
c = int(input("hgow many symbols would you like to insert \n"))
password = []
for i in range(1,a+1):
    password+=random.choice(alphabets)
for i in range(1,b+1):
    password+=random.choice(numbers)
for i in range(1,c+1):
    password+=random.choice(symbols)
#print(password)
random.shuffle(password)
print (password)
new_password = " "
for i in password:
    new_password+=i
print(f"yur hard password is {new_password}\n")

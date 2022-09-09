#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easyPassword=[]
for i in range(nr_letters):
  easyPassword.append(random.choice(letters))
for i in range(nr_numbers):
  easyPassword.append(random.choice(numbers))
for i in range(nr_symbols):
  easyPassword.append(random.choice(symbols))
print("Easy Level of random password \n")
print("".join(easyPassword))
random.shuffle(easyPassword)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
print("\nHard Level of random password \n")
print("".join(easyPassword))

---------------------------------------------------------------------
OUTPUT:
Welcome to the PyPassword Generator!
How many letters would you like in your password?
15
How many symbols would you like?
5
How many numbers would you like?
4
Easy Level of random password 

MluedUVmNBjhxGK1406&!!*$

Hard Level of random password 

$duMehl641*BKVU!N!jGm&x0
 

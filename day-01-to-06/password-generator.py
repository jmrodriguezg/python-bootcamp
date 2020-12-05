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


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#import random

nr_total = nr_letters + nr_symbols + nr_numbers

password=""
cant_let=len(letters) - 1
cant_num=len(numbers) - 1 
cant_sym=len(symbols) - 1

nro_let = 0
nro_num = 0
nro_sym = 0

#old school version
i=1
while i <= nr_total:
  caracter = random.randint(1,3)
  if caracter==1 and nro_let < nr_letters:
    #letters
    password += letters[random.randint(0,cant_let-1)]
    nro_let += 1
    i += 1
  elif caracter==2 and nro_num < nr_numbers:
    #numbers
    password += numbers[random.randint(0,cant_num-1)]
    nro_num += 1
    i += 1
  elif caracter==3 and nro_sym < nr_symbols:
    #symbols
    password += symbols[random.randint(0,cant_sym-1)]
    nro_sym += 1
    i += 1

print (password)

#new school version
password_list=[]
for car in range(1, nr_letters+1):
    password_list.append(random.choice(letters)) 
for car in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers)) 
for car in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols)) 

random.shuffle(password_list)

password=""
for car in password_list:
    password += car

print (password)
# Password Generator
import random
Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*(){}[]+-_"


passwrd_len1 = input("What length would you like your password to be: ")
passwrd_count1 = input("How many passwords would you like : ")
passwrd_len = int(passwrd_len1)
passwrd_count = int(passwrd_count1)
for x in range(0, passwrd_count):
     password = ""
     for x in range(0, passwrd_len):
         password_char = random.choice(Chars)
         password = password + password_char

     print(password)

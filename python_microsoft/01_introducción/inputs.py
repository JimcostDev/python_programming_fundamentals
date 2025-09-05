
#ejecutar en bash con este nombre
#python inputs.py 2022-06-09 
import sys

print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg


print("Welcome to the greeter program")
name = input("Enter your name ")
print("Greetings: " + name)

print("calculator program")
first_number = int(input("first number: "))
second_number = int(input("second number: "))
print(first_number + second_number)

# print('1'+ 2)
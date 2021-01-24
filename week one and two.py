# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:05:02 2021

@author: arinola.ajudua
"""


week one tasks 
need help on this one?
 import random
 
def randomNumberList(0, 100, 2):
   result=[]
   
   for i in range (1, 100):

   temp = random.randint(1, 100+1)
   result.append(temp)
   
   return result 
   
   no = int(input('how many numbers do you wish to generate in a list?'))
   start = int(input('what is the starting range?'))
   end  = int(input('what is the ending range?'))
   
   print('Generatd Number List: {0}'.format(randomNumberList(no, start, end)))

this works

import random

number = random.randint(1,10)

print("the random number is", number)


 Write a program that does the following:
a) Stores a random number (1-10) in a variable – see hint below.
b) Asks a user for their name and stores this in a variable.
c) Asks a user to guess the number between 1 and 10.
d) Tells the user whether they have guessed correctly.
import random
rand_num = random.randint(1,10)
my_name = input("Hello! What is your name?")
guess_number = int(input("Pick a number between 1 and 10. "))
if rand_num == guess_number:
    print ("Well done, you got it right!")
else:
    print("You got it wrong, it was", rand_num)



write a programe that asks a user for a favriout number between 1 and 100 
and tells them a joke based on the nujmber min of 3 jokes

my_name = input("Hello, what is your name?")
print("Well, " + my_name + " Pick a number between 1 to 100 and I will tell you a joke.")
my_number = int(input("Pick a numner."))
if my_number <=33:
    print("Why didnt the egss cross the road it was to chicken!")
elif my_number >63 and my_number <=48:
    print("I hate the word I becuase I'm in it!")
else:
    print("knock knock whoos there?!")


Write a program that allows user to enter their favourite starter, main course, dessert and drink.

starter = input("What is your favourite starter?")
main = input("What is your favourite main meal?")
dessert = input("What is your favourite dessert?")
drink = input("What is your favourite drink?")
print("Your favourite meal is " + starter + ", " + main + "and " + dessert + " with a glass of " + drink + ".")



A motorbike costs £2000 and loses 10% of its value every year. Using a loop, 
print the value of the bike every following year until it falls below £1000.

bike = 2000
while bike >900:
    print("The value of the bike is:", bike)
    bike *= 0.9

Write a program which will ask for two numbers from a user. 
Then offer a menu to the user giving them a choice of operator

number1 = int(input("What is your first number?"))
number2 = int(input("What is your second number?"))
operator = input("What is your operator of choice +,-,/,*,**,%,//: ")
if operator == "+":
    print(number1+number2)
elif operator == "-":
    print(number1-number2)
elif operator == "*":
    print(number1*number2)
elif operator == "/":
    print(number1/number2)
elif operator == "**":
    print(number1**number2)
elif operator == "//":
    print(number1//number2)
elif operator == "%":
    print(number1%number2)
else:
    print("Invalid operator chosen")

As an extension to the motorbike task that costs £2000 and loses 10% of its 
value every year. Using a loop, print the value of the bike every following 
year until it falls below £1000 by using a function and passing in parameters.


def procedure1(inp_bike):
    bike = inp_bike
    print("The value of the bike is:", bike, "The value of the bike will decrease by 10 percent each year.")

bike = int(input("What is the value of the bike?"))

procedure1(bike)

while bike >900:
    print("The value of the bike is:", bike)
    bike *= 0.9
    
    
    
 Write a program which will ask for two numbers from a user. Then offer a menu to the user giving them a choice of maths operators. Once the user has selected which operator they wish to use, perform the calculation by using a procedure and passing parameters.
print("Pick two numbers and math operator and I will complete the calculation.")

def procedure_2(inp_num_1, inp_num_2, inp_op):
    number1 = inp_num_1
    number2 = inp_num_2
    operator = inp_op
number1 = int(input("What is your first number?"))
number2 = int(input("What is your second number?"))
operator = input("What is your operator of choice +,-,/,*,**,%,//: ")

procedure_2(number1, number2, operator)

if operator == "+":
    print(number1+number2)
elif operator == "-":
    print(number1-number2)
elif operator == "*":
    print(number1*number2)
elif operator == "/":
    print(number1/number2)
elif operator == "**":
    print(number1**number2)
elif operator == "//":
    print(number1//number2)
elif operator == "%":
    print(number1%number2)
else:
    print("Invalid operator chosen")

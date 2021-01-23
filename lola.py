# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:05:02 2021

@author: arinola.ajudua
"""

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


import random

number = random.randint(1,10)

print("the random number is", number)

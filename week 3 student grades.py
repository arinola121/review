# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 10:55:39 2021

@author: arinola.ajudua
"""

week 3 studenr grades


def mark_grade():

  mark_grade = int(input("So go on then, what % did you get in the test? "))

  if (mark_grade >= 85):
    print ("wow, you got an A?! amazing work !")
  elif (mark_grade >=75 and mark_grade <85):
    print ("great work, B good work.")
  elif (mark_grade>= 65 and mark_grade<75):
    print ("C good effort.")
  elif (mark_grade >= 55 and mark_grade <65):
    print ("Grade D, you put some effort it but try harder next time.")
  elif (mark_grade >=0 and mark_grade <55):
    print ("you fail, please schedule re sit.")
  
  else:
    print ("not applicable.")


  target_grade = int(input("what is your target % ? "))

  if target_grade < mark_grade:
    print ("Your achieved grade is over your target grade.")
  elif target_grade == mark_grade:
    print (" You hit your target  grade!")
  elif target_grade > mark_grade:
    print (" you did not achieve your target grade.")

mark_grade()
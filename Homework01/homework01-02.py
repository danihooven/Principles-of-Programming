""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Homework 01 - Question 02

Please debug the following code, explain what is wrong with it, and fix it?
Fix the code and turn in the corrected program.

@author: Dani Hooven
@version: 09/08/2020

-------------------------------------------------------------------------------------------------------------------- """


# ask the user for the time now (in hours)
# ask for the number of hours to wait for the alarm
# ** correction: convert to integer **
current_time = int(input("What is the current time (in hours 0 - 23): "))
wait_time = int(input("How many hours do you want to wait: "))

# ** correction: removed unnecessary output **
# print(current_time)
# print(wait_time)

# figure out what time it will be
# ** correction: added the remainder operator for 24 hours
final_time = (current_time + wait_time) % 24

# output time when alarm goes off
# ** correction: added string to output for clarity
print("The time will be '", final_time, "hours ' when the alarm goes off.")

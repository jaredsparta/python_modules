import random
import math

### TASK ###
# Use ceil and float from math to make a round function

def round_task():
    choice = input("Input a number to check: ")
    checker = float(choice) % 1
    if checker >= 0.5:
        return print(math.ceil(float(choice)))
    else:
        return print(math.floor(float(choice)))

## os module 
import os, datetime, sys

working_dir = os.getcwd()
print(working_dir)

# # Does not work in windows
# print(os.uname())

print(os.cpu_count()) # Prints number of CPU cores

print(datetime.datetime.today()) # Returns current system datetime

print(sys.path) # Allows one to see system paths

print()
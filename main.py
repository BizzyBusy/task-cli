import sys
from helper import *

input = sys.argv

def main():
    for i, val in enumerate(input):
        print(f"At index {i}, we have argument {val}")

main()



#TODO: each task should have the following properties to keep track of in a JSON file

# id: A unique identifier for the task

# description: A short description of the task

# status: The status of the task (todo, in-progress, done)

# createdAt: The date and time when the task was created

# updatedAt: The date and time when the task was last updated


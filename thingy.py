#!/usr/bin/env python
# Above is the shebang 
name = "Zachary Waldron"
id = 1234567

def otherThings():
    # Gets all characters before the first space
    # A.K.A. First Name
    tmp = name.split(" ")[0]
    print()
    for chars in tmp:
        print(chars)
def particularThings():
    print()
    print("My name all capitalized is " + name.upper())
def summerPlans():
    my_summer_plans = ["sleep", "eat", "drink", "work", "sleep more", "game", "travel"]
    plan = ""
    for thing in my_summer_plans:
        plan = plan + thing + ", " if not(thing == my_summer_plans[len(my_summer_plans) - 1]) else plan + "and " + thing
    print("This summer I plan to " + plan + ".")
def printThings():
    print("My name is " + name)
    print("My student ID is " +str(id))
    otherThings()
    particularThings()
    summerPlans()
if __name__=="__main__":
    printThings()

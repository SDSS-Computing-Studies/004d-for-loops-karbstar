#! python3
"""
###### Task 2
Ask the user to enter a name.
Check the name against a tuple that contains a series of names to see if it is a match. Use a for loop this time instead of a single if with multiple
logical operators
(2 points)

inputs:
str name

outputs:
"That name is in the list"
"That name is not in the list"

example:
Enter a name: Grace
That name is not on the list

example:
Enter a name: Lebron
That name is on the list
"""
r=0
x=input("enter a name=>").strip()
nameList = ("Lebron","Kobe","Michale","Shaq","Dennis")
for i in nameList:
    if i == x:
        print("That name is on the list")
    else:
        r=r+1
        if r == 5:
            print("That name is not on the list")
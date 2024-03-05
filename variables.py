# python print() statement

_cars = 23
cars = 24

CARS = 25
CARS = 23456

numbers_of_cars = 23
kind_of_cars = "Ferrari"

# To see the output:

print(cars)
print(_cars)
print(kind_of_cars)
print(CARS)
print(numbers_of_cars)

# Strings

"""
This is a multi-line comment
You can use this kind of comment to
make longer notes as you are learning.
In python, these are often used as 
docstrings. 

We will do formatting now.
"""

name = "Janelle Jones"
type_of_car = "Rolls Royce"
school = "Foundation Elementary School"

print(name + school) #Not good. No formatting

print(name + " " + school) #Not so good

print(name + " works at " + school + ".") # Still not so good

#python string.format() - This is nice
print("{} works at {} .".format(name,school))

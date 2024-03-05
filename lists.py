# Two lists:
fruits = ["peaches", "apples", "pears", "apples"]
years = [3, "1998", 2.5, 987, "1994"]
print(fruits, years)

# To check membership of an item in a list:
print("apples" in fruits) # Result will be True or False

# Count function
print(fruits.count("apples"))

print(fruits.index("apples"))


'''
# To add an item to a list
fruits.append("oranges")
print(fruits)

#To add a list to a list
fruits.extend(years)
print(fruits)

#Remove item from list. Important to use an exact match to an item in the list
fruits.remove("oranges")
print(fruits)

#To use index when removing item from a list
fruits.pop(0)
print(fruits)

#How to remove the last item in i list, without know how many items are in the list
fruits.pop(-1)
print(fruits)

#Sorting. Can only sort items in a list with like types
#fruits.sort(fruits) # Will fail, since the list has both integers and strings. However,
#However, you can combine int and float for an example
numbers = [5, 1928, 4, 17, 68]
numbers.sort()
print(numbers)

numbers1 = [5, 1928, 4, 17, 68, 97.134]
numbers1.sort()
print(numbers1)
'''
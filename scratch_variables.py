# # Basic funtion example
# def addition():
#     a = 10.9
#     b = 45.0
#     print(a + b) # will not print without a function
#
# # Call of a function. Now, the above will print
# addition()

# The above, but with user input

def addition():
    a = int(input("Enter a number. "))
    b = int(input("Please enter another number. "))
    print(a + b)


addition()


def strings():
    c = str(input("Enter a word. "))
    d = str(input("Enter another word. "))
    print("{} {}".format(c, d))


strings()

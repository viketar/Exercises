# Break
# temp_f = 40
#
# while temp_f > 32:
#     print("The water is {} degrees.".format(temp_f))
#     temp_f -= 1
#     if temp_f == 33:
#         break
#
# print("Water freezes at 32 degrees")


# Continue
for i in range(1,11):
    if i == 7:
        print("We're skipping number 7.")
        continue
    print("This is the number {}.".format(i))


# Pass
for i in range(1,11):
    if i == 3:
        pass    # The while loop skips number 3
    else:
        print("The number is {}.".format(i))
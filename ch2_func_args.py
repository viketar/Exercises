# # Postiional arguments
# def user_info(name, age, city):
#     '''This function prints name, age and city
#     from an argument provided to the function'''
#
#     print("{} is {} years old, from {}".format(name, age, city))
#
#
# user_info("Janet", 58, "Oklahoma City")
# user_info(34, "New York") #Missing one required positional argument, will generate error


# Keyword arguments
def user_info(name, age=0, city="Tucson"):
    '''This function prints name, age and city
    from an argument provided to the function.
    If city is not provided, the kwarg stated
    in the function will print instead '''

    print("{} is {} years old, from {}".format(name, age, city))


user_info("Micah")
user_info(age=56, name="Kadeem")
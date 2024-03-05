'''
*args allows a function to take any number of positional arguments.
**kwargs allows a function to take any number of keyword arguments.
Without defining them ahead of time.
'''

# Example
def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}".format(fname, lname, company, email))


application("Jess", "Ingrass", "mail@mail.com", "TeachCode.org", 75000,
            hire_date = "September 2010")
# How do I print the *arg and the **kwargs from the example above??

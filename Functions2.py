def good_day(name):
    print("Good day " + name)

yn = input("Enter your name : ")
good_day(yn)

"""

We can have a value as default as default argument in a function.
If we specify name = “stranger” in the line containing def, this value is used when no
argument is passed.
Example:
def greet(name = "stranger"):
# function body
greet() # name will be "stranger" in function body (default)
greet("harry") # name will be "harry" in function body (passed)

"""
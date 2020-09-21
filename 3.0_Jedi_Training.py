# Sign your name:Daniel Mitchell
# In all the short programs below, do a good job communicating with your end user!
whereto = input("Which program do you want to go to? 1-5: ")
wherenum = int(whereto)

# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
if (wherenum == 1):
    name = input("What is your name?")
    print("Hello " + name + "!")

# 2. Write a program where a user enters a base and height and you print the area of a triangle.
if (wherenum == 2):
    base = input("What is the base of the triangle?")
    basenum = int(base)
    height = input("What is the height of the triangle?")
    heightnum = int(height)
    a = (heightnum * basenum) * 0.5
    astr = str(a)
    print("The area is " + astr)

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
if (wherenum == 3):
    radius = input("What is the radius of the circle?")
    rnum = int(radius)
    circumference = (3.1415*2) * rnum
    cstr = str(circumference)
    print("The Circumference is " + cstr)

# 4. Ask a user for an integer and then print the square root.
if (wherenum == 4):
    integer = input("Input an integer: ")
    num = int(integer)
    sqroot = num ** (0.5)
    sqrt = str(sqroot)
    print("The square root of "+integer+" is " + sqrt)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
if (wherenum == 5):
    mass = input("What is your mass? ")
    acc = input("What is your acceleration? ")
    massn = int(mass)
    accn = int (acc)
    force = (accn * massn)
    print ("Your force is " +str(force))
    print ("Get it???")



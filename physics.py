import math


input_operation = int(input("input test var = "
"test"))

# try-except check for int
try:
    intcheck = int(input_operation)
except:
    intcheck = -1

#a^2 + b^2 = c^2
def pythagorean():
    a = int(input("first var = "))
    b = int(input("second var = "))

    c = math.sqrt(a**2 + b**2)

    print("pythegorean value =", c)
    return c

# A cos (x) && A sin (y)
def component():
    distance = int(input("distance = "))
    angle = input("angle = ")

    x = distance * math.cos(math.radians(angle))
    y = distance * math.sin(math.radians(angle))

    print("x-component = ", x, "y-component = ", y)

# speed // Velocity Formula

def velocity():
    distance = int(input("distance = "))
    time = int(input("time = "))
    
    velocity = distance/time
    
    print("velocity(d/t) =", velocity)

if intcheck == 1:
    pythagorean()
elif intcheck == 2:
    component()
elif intcheck == 3:
    velocity()
else:
    print(intcheck)
    exit: 0
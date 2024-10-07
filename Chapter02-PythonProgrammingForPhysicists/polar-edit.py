# Comment test.

from math import sin,cos,pi

# Ask the user for the values of the radius and angle
r = float(input("Enter r: "))
d = float(input("Enter theta in degrees: "))

# Convert the angle to radians
theta = d*pi/180

# Calculate the equivalent Cartesian coordinates
x = r*cos(theta)
y = r*sin(theta)

# Print out the results
print("x =", x, "y =", y)

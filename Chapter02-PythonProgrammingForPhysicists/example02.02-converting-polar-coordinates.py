from math import sin,cos,pi

r = float(input("Enter r: "))
d = float(input("Enter theta in degrees: "))

theta = d*pi/180 # convert to radians

x = r*cos(theta)
y = r*sin(theta)

print("Cartesian coordinates: x =", x, " y =", y)

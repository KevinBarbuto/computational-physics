# Objective: Write a program that will calculate the time required
# for a ball to hit the ground when dropped from a tower of variable height.


g = 9.81 # m/s^2
h = float(input("Enter the tower's height (m): ")) # m

t = (2*h/g)**(1/2) # s

print(t, "s")

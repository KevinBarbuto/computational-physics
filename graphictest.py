from matplotlib.pyplot import *
from numpy import linspace,sin

x = linspace(0,10,100)
y = sin(x)
plot(x,y)
ylim(-1.1,1.1)
xlabel("x axis")
ylabel("y = sin x")
show()

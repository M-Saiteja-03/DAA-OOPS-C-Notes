from matplotlib.pyplot import *
from numpy import *
t=linspace(1,5,20)# in numpy
print(t)
plot(t,sin(t))# plot in pyplot
title("sin curve")
show()

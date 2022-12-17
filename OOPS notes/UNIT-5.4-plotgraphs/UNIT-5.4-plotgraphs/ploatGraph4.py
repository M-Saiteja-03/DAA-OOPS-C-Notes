from matplotlib.pyplot import *
from numpy import *
x=linspace(1,5,100)# in numpy
plot(x,-x*x+4*x-5,'g',linewidth=3)# graph in red color
show()

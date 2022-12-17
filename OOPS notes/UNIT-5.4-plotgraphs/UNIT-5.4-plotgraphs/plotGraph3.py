from matplotlib.pyplot import *
from numpy import *
x=linspace(1,5,100)# in numpy
y=(sin(x)*sin(x))/x
plot(x,y,'g+',linewidth=4)# graph in red color
show()

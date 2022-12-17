from matplotlib.pyplot import *
from numpy import *
x=linspace(0,50,20)
subplot(2,1,1)
plot(x,sin(x),'r')
title("sin(x)")
y=linspace(0,50,20)
subplot(2,1,2)
plot(y,cos(y),'g')
title("cos(y)")
show()

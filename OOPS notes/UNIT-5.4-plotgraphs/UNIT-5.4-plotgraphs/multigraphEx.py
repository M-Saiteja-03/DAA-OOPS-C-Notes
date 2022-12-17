from matplotlib.pyplot import *
from numpy import *
x=linspace(0,50,20)
y=linspace(0,20,200)
plot(x,sin(x),'r')
plot(y,cos(y),'b')
legend(['sin(x)','cos(y)'])
xlabel('X-axis')
ylabel('Y-axis')
show()

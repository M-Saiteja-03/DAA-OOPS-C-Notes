from matplotlib.pyplot import *
from numpy import *
year,profit=loadtxt("test.txt",unpack=True)
pie(profit,labels=year,colors=['r','b','g'])
show()

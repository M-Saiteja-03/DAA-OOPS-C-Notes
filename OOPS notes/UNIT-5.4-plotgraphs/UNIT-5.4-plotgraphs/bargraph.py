from matplotlib.pyplot import *
from numpy import *
year,profit=loadtxt("test.txt",unpack=True)

bar(year,profit)
show()
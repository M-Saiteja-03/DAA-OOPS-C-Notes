from matplotlib.pyplot import *
from numpy import *
year,profit=loadtxt("company-a-data.txt",unpack=True)

bar(year,profit,fill=False,hatch='/')
show()

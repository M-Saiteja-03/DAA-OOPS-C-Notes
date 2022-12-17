from matplotlib.pyplot import *
from numpy import *
year,profit=loadtxt("temp.txt",unpack=True)
print(year)
print(profit)
scatter(year,profit,color='r')
xlabel('year')
ylabel('profit')
show()

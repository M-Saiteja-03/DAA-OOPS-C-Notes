from matplotlib.pyplot import *
from numpy import *
year,profit=loadtxt("company-a-data.txt",unpack=True)
print(year)
print(profit)
scatter(year,profit,color='r',marker='+')
xlabel('year')
ylabel('profit')
show()

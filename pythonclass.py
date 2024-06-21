from turtle import color
from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np

xp=np.array([1,2,6,8])
yp=np.array([30,25,55,50])     
ylabels=["A","B","C","D"]
x=np.random.normal(100,25,200)
# plt.subplot(1,2,1)
# plt.plot(xp,linestyle='dotted',marker='o',ms=10,mfc='r',mec='r')
# plt.title("GRAPH")
# plt.xlabel("Time")
# plt.ylabel("Tension")
# plt.grid()
# plt.subplot(1,2,2)
# plt.plot(xp,linestyle='dotted',marker='o',ms=10,mfc='r',mec='r')
# plt.scatter(xp,yp)
# plt.bar(xp,yp,color="red")
# plt.title("GRAPH")
# plt.xlabel("Time")
# plt.ylabel("Tension")
# plt.grid()
plt.pie(yp,labels=ylabels)
plt.legend(title="ALPHABETS")
plt.show()
str=input()
s=str.count('')
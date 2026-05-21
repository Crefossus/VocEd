#simple plots for playing with matplotlib
import matplotlib.pyplot as plt
import numpy as np


x = [21,22,23,24,25,26]
y = [110,151,138,145,120,114]


fig,ax = plt.subplots()
ax.set_ylabel("students")
ax.set_xlabel("year")
plt.plot(x,y)
plt.show()
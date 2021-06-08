#%%
import matplotlib.pyplot as plt
import numpy as np
x = np.array([0,60])
y = np.array([1,30])

plt.plot(x,y)
plt.show()
#%%
y = np.array([1,3,5,23])

plt.plot(y,marker='*', ms = 20, mec = 'r',mfc = 'y')
plt.show()
# 'o','X','>','1',etc can be used as markers
#ms is the marker size n mec=marker egde color ,mfc=marker face color
#%%
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x, y,c=colors, cmap='viridis')
plt.colorbar()

plt.show()
#%%
x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 
#%%

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.3, 0, 0, 0]
mycolors = ["black", "hotpink", "b", "g"]
plt.pie(y, labels = mylabels,startangle = 90, explode = myexplode, shadow = True,colors = mycolors)
plt.legend(title='Fruits')
plt.show() 
#%%
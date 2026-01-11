import matplotlib.pyplot as plt
import numpy as np;
# x = np.arange(1,10)
# y = x*x
# plt.plot(x,y)
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title('Line Plot')
# plt.show()
# plt.savefig('line_plot.png')


## bar plot
x = [2,4,6]
y = [12,6,8]

x2 = [5,10,25]
y2 = [10,24,12]
plt.bar(x,y)
plt.bar(x2,y2,color = 'g')
plt.show()
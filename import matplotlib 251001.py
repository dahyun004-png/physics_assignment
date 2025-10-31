import matplotlib.pyplot as plt

x=[1,2,3]
y=[3,1,4]
z=[3,2,3]

#plt.scatter(x,y,marker='s', c='b', edgecolors='r')

plt.plot(x,y, marker= 's', markeredgecolor='r', markerfacecolor='g', label='y')
plt.plot(x,z, marker='s', ls='--', mec='k', mfc='w', label='z')
plt.legend(loc='lower right')
# plt.scatter(x,y, marker='p', c='y', edgecolors='r')
plt.show()
import matplotlib.pyplot as plt
marks=[45,50,67,56,76,89,9,83]
plt.hist(marks,bins=[0,20,40,60,80,100],color='purple',edgecolor='black')
plt.title("histogram ")
plt.xlabel("marks")
plt.ylabel("number")
plt.show()
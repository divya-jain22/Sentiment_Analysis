# To visualize the output the following code will work
# Here we have used matplotib library to visualize the data
# The code will genetate the output as given as in file visual.png

from matplotlib import pyplot at plt
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()

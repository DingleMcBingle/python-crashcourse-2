import matplotlib.pyplot as plt

#This Covers 15-2 as well.

x_values = list(range(5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# Set chart title and label axes.
plt.title("Cubes", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of value", fontsize=14)

# Set the range for each axis.
plt.axis([0,5100, 0, 5100**3])

# Set the size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
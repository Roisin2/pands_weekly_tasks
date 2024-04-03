# weekly task HISTOGRAM of Normal Disribution 
# Author :Roisin Stanley

# Import Libraries.
import numpy as np
import matplotlib.pyplot as plt

# mean is 5, deviation is 2 and 1000 values. (generating 1000 random values)
values = np.random.normal(5, 2, 1000)

# Create Histogram - random values, number of bins, display normal density,transparancy of bars, label.
plt.hist(values, bins = 30, density = True ,alpha = 0.6, color = "yellow", label = " Normal Distribution")

# Define the function h(x)=x^3.
def  h(x):
    return x**.3

# Create an array of values in the range [0,10]
x_values = np.linspace(0, 10, 100) #100 points evenly spaced between 0 and 10

# Plot h(x) on same axes.
plt.plot(x_values, h(x_values), color = "purple", label = "h(x) =x^3")

# Add Labels and a Legend
plt.xlabel("X")
plt.ylabel("Y or Density")
plt.title("Histogram of Normal Distribution and (hx) = x^3")
plt.legend()

# Add a grid  https://www.w3schools.com/python/matplotlib_grid.asp
plt.grid(color = 'g', linestyle = '--', linewidth = 0.5 )


# Show the plot.
plt.show()




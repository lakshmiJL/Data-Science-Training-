import matplotlib.pyplot as plt
import numpy as np

#LINE PLOT

# Show the easiest graph (y = x)
x = np.arange(2,11,2)
y = 2*x + 3

plt.figure(figsize=(6,3))
plt.title("Line Plot")
plt.plot(x, y, 'g--^', linewidth = 4, label = " Y = 2X + 3")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
#plt.axis([0, 10, 0, 50])
plt.xticks(ticks=x, labels=x, rotation = 45)
plt.legend()
plt.show()

# Formatting

#plt.figure(figsize=(6,3))
#plt.title("Line Plot")
#plt.plot(x, y, 'ro', label = " Y = 2X + 3", linewidth = 4) g^, r--, b--, b-, p-
#plt.legend()
#plt.xlabel("X-axis")
#plt.ylabel("Y-axis")
#plt.axis([0, 10, 0, 50])
#plt.xticks(ticks=x, labels=x, rotation = 45)

# Plot multiple graphs on a single plot
plt.plot(x, x**2, 'r', label="Y = X**2", linewidth = 3)
plt.plot(x, x**3, 'g', label="Y = X**3", linewidth = 3)
plt.legend()
plt.show()

#How to get smoother curve?
#x = np.linspace(1,5,20)

#BAR PLOT
# x cordinate = position of bar
# y cordiante = length of bar

plt.bar([1,3,5,7], [2,6,4,9], color = 'b')
plt.show()

# Showing multiple graphs in a single plot
plt.bar([1,3,5,7], [2,6,4,9], color = 'b')
plt.bar([2,4,6,8], [3,5,7,9], color = "m")
plt.show()

# Showing the categorical data using bar plot
plt.bar(["Male Literacy", "Female Literacy"], [90, 95])
plt.show()

#Task - Plot the graph of count of passengers in different Pclass on a bar plot

#HISTOGRAM
ages = [22,55,36,45,21,67,45,23,89,11,33,72,88,67,89,12,6,9,48,75,18] #values
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] #intervals

plt.hist(ages, bins, rwidth = 0.8) #rwidth The relative width of the bars as a fraction of the bin width. 
plt.xlabel("Age Interval")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()

#SCATTER PLOT
plt.scatter(x, y, label = "Scatter Plot", color = 'red', marker = 'o', s = 50)
plt.show()

#PIE CHART
slices = [7, 2 ,10, 2, 3]
activities = ["sleeping", "eating", "working", "netflix", "workout & friends"]

cols = ['c', 'm', 'r', 'b', 'g']

plt.pie(slices, labels = activities, colors = cols, autopct='%1.1f%%', startangle = 90, shadow = True)# colors = cols, startangle = 90, shadow = True , autopct='%1.1f%%'
plt.title("Day Chart")
plt.show()

#STACK PLOT
days = ["Mon","Tue","Wed","Thu","Fri"]

languages = [2,3,1,3,1]
sciences = [1,2,1,2,3]
math = [2,1,2,3,2]
others = [3,2,4,0,2]

plt.stackplot(days, languages, sciences, math, others, colors = ['m','c','r','k'],labels=["Language", "Sciences", "Math", "Others"])

plt.xlabel("x")
plt.ylabel("y")
plt.title("Stack Plot")
plt.legend()
plt.show()

#SUB PLOTS
def f(t):
  return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0, 5, 0.1)
t2 = np.arange(0, 5, 0.02)

plt.figure()
plt.subplot(232)
plt.plot(t1, f(t1), 'bo')

plt.subplot(234)
plt.plot(t2, np.cos(2*np.pi*t2))

plt.show()

#Task - Plot the pie chart of count of passengers in different Pclass.
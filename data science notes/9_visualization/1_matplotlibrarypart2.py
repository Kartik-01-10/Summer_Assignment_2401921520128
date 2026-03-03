import matplotlib.pyplot as plt
import numpy as np  

# scatter() function is used to create scatter plots
# it plot for each observation in the data
# x = np.array([1, 2, 3, 4, 5, 6])
# y = np.array([5, 7, 4, 6, 8, 7])
# plt.scatter(x, y, color='g', marker='x') # marker is used to change the shape of the marker
# plt.show()

# now we will compare plot on same fig
# x = np.array([1, 2, 3, 4, 5, 6])
# y = np.array([5, 7, 4, 6, 8, 7])
# plt.scatter(x, y,)
# x = np.array([1, 2, 3, 5 , 7, 9])
# y = np.array([3, 5, 2, 4, 6, 5])
# plt.scatter(x, y,)
# plt.show() # here by default different colors are assigned to different plots are blue and orange
# we can also assign colors to different plots 
# using color parameter in scatter function
# plt.scatter(x, y, color='r') # here all points will be red

# we can change particular point color using array of colors
# x = np.array([1, 2, 3, 4, 5, 6])
# y = np.array([5, 7, 4, 6, 8, 7])
# colors = np.array(['red', 'blue', 'green', 'yellow', 'black', 'orange'])
# plt.scatter(x, y, c=colors)
# we have one more thing as colormap
# colormap is used when we have large number of points  
# colors = np.array([0, 10, 20, 30, 40, 50])
# plt.scatter(x, y, c=colors, cmap='viridis')
# plt.show()


# we can also change size of marker using s parameter
# x = np.array([1, 2, 3, 4, 5, 6])
# y = np.array([5, 7, 4, 6, 8, 7])
# sizes = np.array([20, 50, 80, 200, 500, 1000]) # size of each marker
# plt.scatter(x, y, s=sizes)
# plt.show()
# we can also change size and color together
# x = np.array([1, 2, 3, 4, 5, 6])
# y = np.array([5, 7, 4, 6, 8, 7])
# sizes = np.array([20, 50, 80, 200, 500, 1000]) # size of each marker
# colors = np.array([0, 10, 20, 30, 40, 50])
# plt.scatter(x, y, s=sizes, c=colors, cmap='viridis')
# plt.show()
# with this add colorbar
# x = np.array([1, 2, 3, 4, 5, 6])
# y = np.array([5, 7, 4, 6, 8, 7])
# sizes = np.array([20, 50, 80, 200, 500, 1000]) # size of each marker
# colors = np.array([0, 10, 20, 30, 40, 50])
# plt.scatter(x, y, s=sizes, c=colors, cmap='viridis')
# plt.colorbar() # show color scale outside the plot
# plt.show()

# alpha : is used to set the transparency level of the markers
# x = np.array([1, 2, 3, 4, 5, 6])
# y = np.array([5, 7, 4, 6, 8, 7])
# sizes = np.array([20, 50, 80, 200, 500, 1000]) # size of each marker
# colors = np.array([0, 10, 20, 30, 40, 50])
# plt.scatter(x, y, s=sizes, c=colors, cmap='viridis', alpha=0.5)
# plt.colorbar() # show color scale outside the plot    
# plt.show()
# here alpha value 0.5 means 50% transparent markers
# alpha value 0 means fully transparent
# alpha value 1 means fully opaque markers


# x = np.random.randint(100, size = (100))
# y = np.random.randint(100, size = (100))
# colors = np.random.randint(100, size = (100))
# sizes = 10 * np.random.randint(100, size = (100))
# plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
# plt.colorbar()
# plt.show()


# now we will create vertical bar chart using bar() function
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([5, 7, 4, 6, 8])
# plt.bar(x, y)
# plt.show()


# now we will create horizontal bar chart using barh() function
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([5, 7, 4, 6, 8])
# plt.barh(x, y)    
# plt.show()


# customize the bar chart
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([5, 7, 4, 6, 8])
# plt.bar(x, y, color='cyan', edgecolor='black', width=0.5)
# plt.show()


# now we will create histogram using hist() function
# data = np.random.randint(1000, size=(1000)) # generate 1000 random numbers   
# plt.hist(data, bins=30, color='blue', edgecolor='black', alpha=0.7)
# plt.show()



# creating pie chart using pie() function

# y = np.array([20, 30, 25, 15, 10])
# labels = ['A', 'B', 'C', 'D', 'E']
# plt.pie(y, labels=labels)
# plt.show()

# startangle parameter - the default start angle is at 0 degree (3 o'clock position)
# but we can change it using startangle parameter by providing angle in degree
# y = np.array([20, 30, 25, 15, 10])
# labels = ['A', 'B', 'C', 'D', 'E']
# plt.pie(y, labels=labels, startangle=90) # here start angle is 90 degree
# plt.show()


# labels = ['A', 'B', 'C', 'D', 'E']
# sizes = [20, 30, 25, 15, 10]  
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen']
# explode = (0.1, 0, 0, 0, 0) # explode 1st slice
# plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
# plt.axis('equal') # equal aspect ratio ensures that pie is drawn as a circle  
# plt.show()
# autopct parameter is used to display percentage value on each slice
# shadow parameter is used to add shadow effect to the pie chart
# plt.axis('equal') is used to ensure that pie chart is a circle    
# explode parameter is used to "explode" or offset a slice from the pie chart

# we can also add legend to pie chart
labels = ['A', 'B', 'C', 'D', 'E']    
sizes = [20, 30, 25, 15, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen']
explode = (0.1, 0, 0, 0, 0) # explode 1st slice
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal') # equal aspect ratio ensures that pie is drawn as a circle
plt.legend(title="Categories", loc="best")
plt.show()# here legend() function is used to add legend to pie chart
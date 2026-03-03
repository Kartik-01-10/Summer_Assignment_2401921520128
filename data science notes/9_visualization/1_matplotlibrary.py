import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# print ("Matplotlib version:", matplotlib.__version__)
# print ("Numpy version:", np.__version__)

# xpoint = np.array([0, 6])
# # xpoint = np.array ([0, 1, 2, 3, 4, 5, 6])
# ypoint = np.array([100, 250])


# here we are labeling the plot with title and x and y axis labels
# plt.plot(xpoint, ypoint)
# plt.title("Sample Line Plot")
# plt.xlabel("X Axis Label")
# plt.ylabel("Y Axis Label")
# plt.show()


# x = np.array([0, 1, 2, 3, 4, 5])
# y = np.array([0, 1, 4, 9, 16, 25])
# plt.plot(x, y,'o')
# plt.show()

# plt.plot(x,y, '+')
# plt.show()

# format string "fnt" - marker, line, color
# marker: . , o , v , ^ , < , > , s , + , x , D , d , | , _ 
# line: - , -- , -. , : 
# color: b , g , r , c(cyan) , m(magenta) , y , k(black) , w(white) 

# plt.plot(x, y, 'o-.r')
# plt.show()

# marker size 
# y = np.array([0, 1, 4, 9, 16, 25])
# here it will take by default value of x as [0, 1, 2,... acc to length of y]
# plt.plot( y, 'o-.r', markersize=10) # or use as ms = 10
# plt.show()

# plt.plot( y, 'o-.r', markerfacecolor='blue', markeredgewidth=3)
#markerfacecolor=mfc # it means color of inner part of marker
# plt.show()
# marker edge width  markeredgewidth = mew # it means color of outer lining of marker
# plt.plot( y, 'o-.r', mew=5)


# linestyle or ls : is used to change the style of the plotted line
# ls = '-' (solid line)
# ls = '--' (dashed line)
# ls = '-.' (dash dot line)
# ls = ':' (dotted line)
# plt.plot( y, color='green', ls='--', marker='o', markersize=10)
# plt.plot( y, color='green', linestyle='dashed', marker='o', ms=10)
# plt.show()

# linewidth or lw : is used to change the width of the plotted line
# plt.plot( y, color='green', linestyle='dashed', marker='o', ms=10, lw=5)
# plt.show()

# color : is used to change the color of the plotted line
# plt.plot( y, color='#4CAF50', linestyle='dashed', marker='o', ms=10, lw=5)
# plt.show()

# for multiple lines in single plot
# y1 = np.array([0, 1, 4, 9, 16, 25])
# y2 = np.array([0, 1, 2, 3, 4, 5])
# plt.plot( y1, color='green', linestyle='dashed', marker='o', ms=10, lw=5)
# plt.plot( y2, color='blue', linestyle='dotted', marker='x', ms=10, lw=5)
# plt.show()
# here we get two lines in single plot with different styles
# here also it is taking default value




# for legend in plot
y1 = np.array([0, 1, 4, 9, 16, 25])
y2 = np.array([0, 1, 2, 3, 4, 5])
# plt.plot( y1, color='green', linestyle='dashed', marker='o', ms=10, lw=5, label='Squared Numbers')
# plt.plot( y2, color='blue', linestyle='dotted', marker='x', ms=10, lw=5, label='Linear Numbers')
# plt.legend()    
# plt.show()
# here legend() function is used to show the labels of different lines in plot


# now we will set the font properties for title and labels
# font1 = {'family':'serif', 'color':'blue', 'size':20}
# font2 = {'family':'serif', 'color':'darkred', 'size':15}  
# plt.plot( y1, color='green', linestyle='dashed', marker='o', ms=10, lw=5, label='Squared Numbers')
# plt.plot( y2, color='blue', linestyle='dotted', marker='x', ms=10, lw=5, label='Linear Numbers')
# plt.title("Sample Plot", fontdict=font1)
# plt.xlabel("X Axis", fontdict=font2)
# plt.ylabel("Y Axis", fontdict=font2)
# plt.legend()    

# fontdict is used to set the font properties
# now set the position of legend
# plt.legend(loc='upper left') # other options are: upper right, lower left, lower right, right,
#  center left, center right, lower center, upper center, center  

# now set the position of title
# plt.title("Sample Plot", loc='left') # other options are: right, center, default is center
# now set the grid in plot
# plt.grid(color='gray', linestyle='--', linewidth=0.5) 
# if we dont specify any parameter in grid() function then it will take default values
# so for that just use plt.grid()

# here grid() function is used to add grid lines in the plot    
# we can also customize the grid lines acc to x and y axis
# plt.grid(axis='x') # it will show grid lines only for x axis
# plt.grid(axis='y') # it will show grid lines only for y axis
# plt.grid(axis='both') # it will show grid lines for both x and y axis
# in grid the default value of axis is 'both'



# display the multiple plot - with subplots()
x = np.array([0, 1, 4, 9, 16, 25])
y = np.array([0, 1, 2, 3, 4, 5])
# plt.subplot(2, 1, 1) # (rows, columns, panel number)
# plt.plot(x, y, 'o-r')
# plt.title("First Subplot")
# plt.subplot(2, 1, 2)
# plt.plot(y, x, 's--b')
# plt.title("Second Subplot")
# plt.show()
# here we have created two subplots in single figure
# here 2,1,1 means 2 rows, 1 column, first panel
# and 2,1,2 means 2 rows, 1 column, second panel
# means we are dividing the figure into 2 rows and 1 column and placing the plots accordingly   
# plot is divide in two horizontal parts
# we can also divide the plot in vertical parts 
# plt.subplot(1, 2, 1) # (rows, columns, panel number)
# plt.plot(x, y, 'o-r')
# plt.title("First Subplot")
# plt.subplot(1, 2, 2)      
# plt.plot(y, x, 's--b')
# plt.title("Second Subplot")
# plt.show()
# we can also create multiple subplots in more than 2 rows and 2 columns
# plt.subplot(2, 3, 1) # (rows, columns, panel number )
# plt.plot(x, y, 'o-r')

# plt.subplot(2, 3, 2)
# plt.plot(y, x, 's--b')

# plt.subplot(2, 3, 3)
# plt.plot(x, y, 'o-r')

# plt.subplot(2, 3, 4)
# plt.plot(y, x, 's--b')
# plt.subplot(2, 3, 5)
# plt.plot(x, y, 'o-r')

# plt.subplot(2, 3, 6)
# plt.plot(y, x, 's--b')
# plt.show()


# we can also adjust the space between the subplots
plt.subplot(2, 1, 1) # (rows, columns, panel number)
plt.plot(x, y, 'o-r')
plt.title("First Subplot")
plt.subplots_adjust(hspace=0.5)
plt.subplot(2, 1, 2)      
plt.plot(y, x, 's--b')
plt.title("Second Subplot")
plt.show()
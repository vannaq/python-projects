#plt.subplots() when called w/o any inputs creates two differnt objects: a Figure object (container that holds everything you see on page) and an Axes object (part of the page that holds data)
#plotting data on the axes: ax.plot(df["x_axis"], df["y_axis"])
#optional keyword argument lets you add markers to the plot: marker="v" (triangles) or marker="o" (circles)
#linestyle keyword argument lets you change appearance of connecting lines: linestyle="--"
#customize axes labels: ax.set_xlabel("Name") and ax.set_ylabel("name-y")
#add title: ax.set_title("Title Name")
#sharing y-axis: pass argument (sharey=True)
#when you have a NumPy array containing two axes, you need to specify which Axes object you want to use for plotting: e.g. ax[0].plot(df["x_axis"], df["y_axis"], color="b") for top axes and ax[1].plot(df["x_axis"], df["y_axis"], color="r") for bottom axes
#to access the index, particularly in time-series data, use .index attribute

#create a figure and axes, adding data from one variable to the plot then plot two time-series together using twin axes: ax2 = ax.twinx()


#a function that plots time-series: def plot_timeseries(axes, x, y, color, xlabel, ylabel):
#   axes.plot(x, y, color=color)
#   axes.set_xlabel(xlabel)
#   axes.set_ylabel(ylabel, color=color)
#   axes.tick_params('y', colors=color)


#annotations draw attention to a part of the plot by drawing an arrow to that part and including text to explain it -> .annotate("string of text", xy=(pd.Timestamp("date"), y_position) method
#.annotate() method accepts an optional argument to position the text: ax.annotate("string of text", xy=(pd.Timestamp('date'), 1), xytext=(pd.Timestamp('date'), new_y_position))
#add arrows to annotation by adding optional argument: arrowprops={'arrowstyle':'->', 'color':'color'}
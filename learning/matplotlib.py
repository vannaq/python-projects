#plt.subplots() when called w/o any inputs creates two differnt objects: a Figure object (container that holds everything you see on page) and an Axes object (part of the page that holds data)
#plotting data on the axes: ax.plot(df["x_axis"], df["y_axis"])
#optional keyword argument lets you add markers to the plot: marker="v" (triangles) or marker="o" (circles)
#linestyle keyword argument lets you change appearance of connecting lines: linestyle="--"
#customize axes labels: ax.set_xlabel("Name") and ax.set_ylabel("name-y")
#add title: ax.set_title("Title Name")
#sharing y-axis: pass argument (sharey=True)
#when you have a NumPy array containing two axes, you need to specify which Axes object you want to use for plotting: e.g. ax[0].plot(df["x_axis"], df["y_axis"], color="b") for top axes and ax[1].plot(df["x_axis"], df["y_axis"], color="r") for bottom axes
#Seaborn function relplot() stands for relational plot, which enables visualizing the relationship between 2 quantitative variables using either scatter plots or line plots
#advantage over scatterplot() is that it can create subplots in a single figure
#sns.relplot(x="x_axis_variable", y="y_axis_variable", data=dataset, kind="scatter_or_line", col="col_category", row="row_category")
#col_wrap parameter sets how many plots per row before it goes to next row
#col_order and row_order parameters allow for changes to the ordering of subplots based on a list of ordered values

#when creating a scatter plot, control the size of points using the size parameter: sns.relplot(x="x_axis_name", y="y_axis_name", data=datasetname, kind="scatter", size="parameter_for_size")
#control the color of point styles with hue parameter: sns.relplot(x="x_axis_name", y="y_axis_name", data=datasetname, kind="scatter", hue="parameter_for_color")
#setting a point style allows for better differentiation between subgroups: style="parameter_For_style"
#point transparency is set with the alpha parameter, which is a value between 0 and 1: alpha=0.4
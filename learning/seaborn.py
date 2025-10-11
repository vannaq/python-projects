#Seaborn is a python data viz library, developed to easily create common chart types; works well with pandas data structures and built on top of matplotlib

#getting started with scatterplot
#import seaborn as sns
#import matplotlib.pyplot as plt
#sns.scatterplot(x=xlistname, y=ylistname)
#plt.show()

#count plots take in a categorical list & return bars that represent the number of list entries per category
#sns.countplot(x=listname)

#working with pandas DataFrames
#import pandas as pd
#df = pd.read_csv("name.csv")
#df.head() 

#using DataFrames with countplot()
#import pandas, matplotlib, and seaborn
#create a pandas DataFrame from csv file to create the countplot instead of a list of data
#sns.countplot(x="name_of_column_in_df", data=df)
#plt.show()
#Note: Seaborn works great with pandas DataFrames only if the DataFrame is "tidy", meaning each observation has its own row & each variable has its own column
#add color using seaborn's hue argument: hue="smoker"
#set hue order: hue_order=["value", "value2"]
#map hue color using key value: hue_colors={"variable":"color", "Variable2":"color2"}
#adding subgroups: hue="subgroup_name"
#specifying subgroup colors: palette=palette_colors where palette_colors = {"variable": "color"}

#In a line plot, each plot point represents the same "thing" typically tracked over time whereas each point in a scatter plot is an independent observation
#To visualize subgroups: kind="line", style="parameter", hue="parameter"
#Markers parameter set to True will display a marker for each data point: markers=True
#To remove line style for subgroups, set dashes parameter to false: dashes=False
#Given multiple observations per x axis value, seaborn will show aggregate value (Defaults to mean) and the shaded region is the confidence interval
#Use ci parameter to see standard deviation or turn it off: ci="sd" or ci=None

#categorical plots commonly used when making comparisons between different groups: count plots, bar plots
#catplot() used to create categorical plots, with the same flexibility and advantages of relplot, such as col and row paramters
#to create catplot: sns.catplot(x="x_axis", data=dataname, kind="count")
#to change order, list them in desired order before calling seaborn plot and include order parameter. works for all types of categorical plots: category_order = ["item1", "item2", "item3", "item4", "item5"] then sns.catplot(x="x_axis", y="y_axis", data=dataname, kind="bar", order=category_order)

#bar plots display mean of quantitative variable per category: sns.catplot(x="x_axis", y="y_axis", data=dataname, kind="bar")
#seaborn automatically shows 95% confidence intervals for mean so assuming data is a random sample, we're 95% sure the true population mean in each group lies within the confidence interval shown. To no longer display confidence interval: ci=None
#to change orientation of bar plot, swap x and y axis: sns.catplot(y="previous_x_axis_name", data=dataname, kind="bar")


#box plots show the distribution of quantitative data (median, spread, skewness, and outliers) and facilitates comparison between different groups: sns.catplot(x="x_axis", y="y_axis", data=datasetname, kind="box")
#use order parameter to change order of groups displayed
#use the sym paramter to omit outliers: sns.catplot(x="x_axis", y="y_axis", data=datasetname, kind="box", sym="")
#by default, whiskers extend to 1.5*IQR. Change whiskers using whis parameter: whis=2.0   OR to show the 5th and 95th percentile: whis=[5, 95] where the list is [min_value, max_value]

#point plots show the mean of a quantitative variable for the observations in each category, plotted as a single point. It's a categorical plot b/c one axis, usually the x-axis, is a categorical variable whereas a line plot will have quantitative variables for both x and y axes
#use kind parameter to set plot as point plot: kind="point"
#to remove lines connecting the points: join=False
#to have points and confidence intervals calculated for median instead of mean, import median function from numpy library and set estimator equal to numpy median: estimator=median  ---this may be a better stat to use if dataset has a lot of outliers
#to add caps to the end of confidence intervals, set capsize parameter equal to desired width of caps: capsize=0.2 

#changing global figure style for all plots:sns.set_style()  where preset options include "white", "dark", "whitegrid", "darkgrid", "ticks"
#changing figure "palette" changes color of the main elements of the plot: sns.set_palette()  ---use preset palettes or create a custom palette
#changing figure "context" changes the scale of the plot elements and labels: sns.set_context()   ---smallest to largest: "paper", "notebook", "talk", "poster"

#Seaborn's plot functions create 2 different types of objects: FacetGrids and AxesSubplots. assign plot output to a variable and run "type(g)" to see its object type.
#An empty FacetGrid consists of one or more AxesSubplots, which is how it supports subplots
#to assign a title for the figure as a whole: g.fig.suptitle("New Title")
#to adjust height of title, use y parameter: g.fig.suptitle("New Title", y=1.03)  ---note the default value is 1 so 1.03 will make it a little higher

#to add title to AxesSubplot: g.set_title("New Title", y=1.03)
#to add titles for subplots: g.set_titles("This is {col_name}") after setting col parameter to "col_name_variable"
#to add axis labels, assign plot to a variable and call "set" function: g.set(xlabel="New X Label", ylabel="New Y Label")

#to rotate x-axis tick labels, use matplotlib function: plt.xticks(rotation=90)
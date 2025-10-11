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
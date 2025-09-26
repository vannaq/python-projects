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
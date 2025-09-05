#plt is the standard alias for matplotlib.pyplot

#histograms help visualize the distribution of a numeric variable: .hist()
#show plots: plt.show()
#adjust number of bars in histogram using bins argument: .hist(bins=20)

#bar plots can reveal relationships betwn categorical and numerical variable
#bar plots: .plot(kind="bar")
#add title to plot by using title argument: .plot(kind="bar", title="Name of chart")

#line plots are ideal for visualizing changes over time, with x and y axis labels: .plot(x="date", y="weight", kind="line")
#rotating axis labels by passing in angle in degress, such as 45 degrees: (rot=45)

#scatter plots are great for visualizing relationship betwn two numeric variables: kind="scatter"

#layering plots on top of one another: .hist() for plot 1, .hist() for plot 2, then plt.show()
#set a legend to differentiate the plots: plt.legend(["first_attr", "second_attr"])
#set transparency to see what's going on between the plots by passing alpha argument: .hist(alpha=0.8) where 0 means completely transparent and 1 means completely opaque


#missing values can be detected with .isna() which returns a Boolean for every single value indicating whether the value is missing or not
#when working with a lot of data, chain .isna() with .any() to see if there are any missing values in that column
#to count missing values, chain .isna with .sum() to count the number of NaNs in each column
#to remove missing values, use .dropna() which is not ideal if working with a lot of missing data since that means losing a lot of observations
#replace missing values with another value such as 0: .fillna(0)
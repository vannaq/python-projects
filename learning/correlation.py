#correlation -> relationships betwn numeric variables, usually visualized with scatter plots
#correlation coefficient -> a number between -1 and 1 where its magnitude corresponds to strength of relationship (1 is very strong, -1 is not strong)
#Use seaborn, a plotting package built on top of matplotlib: import seaborn as sns
#sns.scatterplot(x="name_of_variable_for_x_axis", y="name_of_variable_for_y_axis", data=DataFrame_name)
#call plt.show() to visualize scatterplot

#adding trendline: sns.lmplot(x="name_of_variable_for_x_axis", y="name_of_variable_for_y_axis", data=DataFrame_name, ci=None) where ci is confidence intervals
#many ways to calculate correlation, one of the most common being Pearson product-moment (r)
#computing correlation with df['x-axis variable'].corr(df['y-axis variable'])
#correlation only accounts for linear relationships -> always visualize your data!

#log transformation can be applied to data that's heavily skewed: df['new_column'] = np.log(df['original_column'])
#correlation does not imply causation
#confounder or confounding variable is a third variable
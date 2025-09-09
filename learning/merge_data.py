#merge_ordered() method can merge time-series and other ordered data
#use it with ordered data / time series and to fill in missing values
#forward fill used to fill in values: pd.merge_ordered(table1, table2, on='common_column', suffixes=('_one', '_two'), fill_method='ffill)


#merge_asof() matches on the nearest key column and not exact matches, therefore whatever columns you merge on must be sorted
# default value for direction argument is "backward" so it'll match on the right key column that is less than or equal to the left key column
#   "forward" will match on the right key column that is greater than or equal to the left key column
#   "nearest" will return nearest row in the right table, regardless if its forward or backwards

#when to use merge_asof(): data sampled from a process and the dates or times may not exactly align, developing a training set where you do not want any events from the future to be visible before that point in time (no data leakage)

##example##
# Merge gdp and recession on date using merge_asof()
# gdp_recession = pd.merge_asof(gdp, recession, on="date")

# # Create a list based on the row value of gdp_recession['econ_status']
# is_recession = ['r' if s=='recession' else 'g' for s in gdp_recession['econ_status']]

# # Plot a bar chart of gdp_recession
# gdp_recession.plot(kind="bar", y='gdp', x='date', color=is_recession, rot=90)
# plt.show()

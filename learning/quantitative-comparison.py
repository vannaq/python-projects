#creating a bar chart: create a figure and axes object then call the axes bar method -> ax.bar(df.index, df['col1'])
#rotate tick labels: ax.set_xticklabels(df.index, rotation=90)

#creating a stacked bar chart to compare data: ax.bar(df.index, df['col2data'], bottom=df["col1"]) then 
#new data is added on top so  we need to tell matplotlib what the bottom comprises of: ax.bar(df.index, df['newcol'], bottom=df['col2data'] + df['col1'])

#add a legend to make the figure easier to understand: 2 steps
#1. add the label keyword to each call of the bar method -> label="color"
#2. add a call to the axes legend method before calling show -> ax.legend()


#histograms: ax.hist(df['colname'])
#to set x-axis label: ax.set_xlabel("name") -- same pattern for y-axis label
#to create labels and set bin boundaries: label='name', bins=#
#transparent histogram that prevents bars from occluding each other: histtype='step' 

#pivot tables are another way to do the same thing as a group-by-then-summarize; it's the standard way of aggregating data in spreadsheets
#by default, pivot tables take the mean value for each group; to use a different summary stat, use aggfunc argument and pass it a function: df.pivot_table(values="column", index="column2", aggfunc="median")

#pivot on two variables: df.pivot_table(values="column_to_summarize", index="column_to_group_by", columns="column_to_group_by_2")
#imputation: replaces missing values with a real value (e.g. fill_value=0 to fill in for NaN)

#margins is a shortcut for when you pivoted by two variables, but also want to pivot by each of those variables separately:(margins=" ") -> results in row and column totals of the pivot table contents

#pivot tables are just dataframes with sorted indexes -> .loc[] + slicing is a power combo
#axis argument, for example df.mean(axis="index"), means "calculate the statistic across rows"
#to calculate summary stat for each row, or across the columns, set axis to "columns": df.mean(axis="columns")

# access the components of a date (year, month and day) using code of the form dataframe["column"].dt.component
#examples: month component is dataframe["column"].dt.month, and the year component is dataframe["column"].dt.year
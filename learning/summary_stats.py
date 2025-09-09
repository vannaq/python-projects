#summarizing numerical data: .median(), .mean(), .mode(), .min(), .max()
#custom summary stats: .agg() which takes a function or string function name as it's parameter, e.g. df['column'].agg(function)
#def pct30(column):
#   return column.quantile(0.3)
#   dataframe["column"].agg(pct30)

#use double square brackets for summaries on multiple columns
#dataframe[["column1", "column2"]].agg(pct30)

#use square brackets for multiple summaries
#dataframe["column"].agg([pct30, pct40])

#note that .agg takes in a function or string function name, so be careful with Python built-in functions like min and max vs. methods named as strings like "mean" and "median"
#do not use quotation marks around user-defined custom functions *reference pct30 above*
#example: df[["column1", "column2"]].agg([iqr, "median"])

#general form of passing a dictionary into .agg() to specify which columns to aggregate: what functions to apply to each:
#df.groupby(...).agg({
#    "column_name_1": "aggregation_function_1",
#   "column_name_2": "aggregation_function_2",
#})


#cumulative stats: .cumsum(), .cummax(), .cummin(), .cumprod()
#example: df["column_name_to_add"] = df["existing_column"].cumsum()


#####Counting#####
#dropping duplicate names: df.drop_duplicates(subset="name")
#dropping duplicate pairs: unique_pairs = df.drop_duplicates(subset=["name", "type"])
#counting number of duplicates: df["type"].value_counts()
#counting number of duplicates, sorted with biggest counts on top: df["type"].value_counts(sort=True)
#normalize=True helps in identifying the share of each category within the total, calculating proportions to understand the relative frequencies of categories: df["column"].value_counts(sort=True, normalize=True)

#group summaries using .groupby("variable")["column"].mean()
#multiple grouped summaries using .agg(): df.groupby("variable")["column"].agg([min, max, sum])
#grouping by multiple variables: df.groupby(["variable1", "variable2"])["column"].mean()
#group by multiple columns and aggregate by multiple columns: df.groupby(["variable", "variable"])[["column1", "column2"]].mean()

#without using .groupby(), calculate totals by using .sum(): sales_all = sales["weekly_sales"].sum()
#calculate total weekly sales for type A stores: sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()
#repeat for type B and C stores, then create a list of totals for A, B, and C to divide by overall total: sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
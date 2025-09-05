#setting a column as the index: df_ind = df.set_index("name")
#removing an index: df.reset_index()
#dropping an index: df.reset_index(drop=True)
#subsetting is cleaner with indexes: df.loc[["name", "name2"]]

#multi-level indexes aka hierarchical indexes; implication that the inner level of index is nested inside the outer level
#to take subset of rows at the outer level index, pass a list of index values to loc: df.loc[["name1", "name2"]]
#subset inner levels with a list of tuples: df.loc[[("attribute1", "attribute2"), ("attribute1", "attribute2")]]

#control sort_index by passing lists to the level and ascending arguments: df.sort_index(level=["attribute1", "attribute2"], ascending=[True, False])

#use .loc when slicing at the outer level of an index: df.loc["row_a":"row_c"]
#do not use .loc when slicing the inner index levels, pandas won't throw an error to let you know there's a problem
#to slice inner index levels correctly, pass the first and last positions as tuples: df.loc[("col1_row1", "col2_row1"):("col1_row4", "col2_row4")]
#since dataframes are 2D objects, can also slice columns: df.loc[:, "column_name1":"column_name2"]
#capable of slicing twice: df.loc[("col1_row1", "col2_row1"):("col1_row4", "col2_row4"), "column_name3":"column_name4"]
#df.loc["row1":"row3", "column1":"column3"] means selecting "row1" through "row3" and "column1" through "column3"


#an important use of slicing is to subset dataframes by a range of dates: df.set_index("date_of_birth").sort_index()
#slice dates with same syntax as other types: df.loc["yyyy-mm-dd":"yyyy-mm-dd"]
#slice by partial dates: df.loc["yyyy":"yyyy"]
#subset by row/column number: df.iloc[2:5, 1:4]
#when selecting consecutive elements using start:end syntax, start is included but end is excluded (for dataframe, this requires sorted indexes)
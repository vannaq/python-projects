#merging tables with inner join is the default (think of venn diagram with left and right dataframes, and the overlapping section in middle): left_table.merge(right_table, on='common_column')
#suffixes help differentiate which table the column came from: left_table.merge(right_table, on='common_column', suffixes=('_left','_right'))

#1:1 relationship is where every row in the left table is related to only one row in the right table
#1 to many relationship is where every row in the left table is related to one or more rows in the right table

#single merge on multiple columns: left_table.merge(right_table, on=['column1','column2'])
#merging multiple tables: left_mid_right_table = left_table.merge(right_table, on=['column1','column2']) \ .merge(mid_table, on='common_column', suffixes=('_left','_right'))  
#note that the backslash line continuation method is important to add the second merge on the next line, otherwise Python will throw syntax error since it'll parse it as 2 lines of code
#to merge more tables, follow the same structure using backslash to instruct Python to read it as one line of code: df1.merge(df2, on='col') \ .merge(df3, on='col') \ .merge(df4, on='col)


#left join is where all rows of data from the left table and only those rows from the right table where key columns match are merged: new_table = left_table.merge(right_table, on='column_name', how='left')

#right join returns all of the rows from the right table and includes on those rows from left table that have matching value (mirror opposite of left join): new_table = left_table.merge(right_table, how='right', left_on='id', right_on='movie_id')
##right joins are useful for ensuring no data is missing from the right table in the result
##merging with different column names using left_on and right_on parameters in the merge method

#outer join returns all of the rows from both tables regardless if there is a match between tables: new_table = left_table.merge(right_table, on='column_name', how='outer', suffixes=('_left', '_right'))
##outer joins particularly useful for finding unmatched data between two tables


#self join, aka merging a table to itself: original_table = sequels_table.merge(sequels_table, left_on='sequel_column_name', right_on='column_name', suffixes=('_orig','_seq'))
#when to merge a table to itself - hierarchical relationships (employee, manager), sequential relationships (logistic movements), graph data (networks of friends)


#merging on indexes: left_right_table = left_table.merge(right_table, on='column_name', how='left')
#multiIndex datasets: df.read_csv('name.csv', index_col=['left_ID', 'right_id'])
#multiIndex merge: df.merge(df2, on=['column1','column2'])
#index merge with left_on and right_on: df_new = df_left.merge(df_right, left_on="column_name", left_index=True, right_on="column_name2", right_index=True)
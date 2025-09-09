#filtering joins: filter observations from table based on whether or not they match an observation in another table 
#semi joins filters the left table down to those observations that have a match in the right table; similar to an inner join where only the intersection between the tables is returned and no duplicates are returned
#3 steps to semi join: 
##  merge left and right tables on key column using inner join: df_merged = df1.merge(df2, on='column_name')
##  search if key column in left table is in the merged tables using .isin() method creating a Boolean series: variable_df = df1[df1['column_name'].isin(df_merged['column_name])]
##  subset rows of the left table

#semi join example -
# Merge the non_mus_tck and top_invoices tables on tid
##tracks_invoices = non_mus_tcks.merge(top_invoices, on='tid')

# Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
##top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group the top_tracks by gid and count the tid rows
##cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':'count'})

# Merge the genres table to cnt_by_gid on gid and print
##print(cnt_by_gid.merge(genres, on='gid'))


#anti joins return the left table, excluding the intersection (meaning it returns observations in the left table that do not have a matching observation in the right table)
#steps to anti join:
##  use left join returning all of the rows from left table: df_merged = df1.merge(df2, on='column_name', how='left', indicator=True)  ##True indicator to the merge method adds a column called "_merge" to the output, which tells the source of each row
##  use loc accessor and "_merge" column to select rows that only appear in the left table & return only the common column from df1 table: column_name_list = df1.loc[df1['_merge'] == 'left_only', 'common_column_name']
##  use .isin() method to filter for rows with column_name in our column_name_list: new_list = df2[df2['common_column_name'].isin(df1['common_column_name'])]

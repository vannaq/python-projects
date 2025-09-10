#.melt() will unpivot a table from wide to long format

#wide format is when every row relates to one subject & each column has different info about an attribute of that subject (easier for people to read)
#long (tall) format is when info about one subject is found over many rows, and each row has one attribute about that subject (more accessible for computers to work with)

#example melting: pd.melt(id_vars=['column1','column2']) where columns are to be used as identifier variables. Note that even if there's only 1 column value in id_vars, use the square brackets
#example2 melting with value_vars: df.melt(id_vars=['column1','column2'], value_vars=['var1','var2']) where value_vars allows us to control which columns are unpivoted, in that order
#example3 melting with column names: df.melt(id_vars=['column1','column2'], value_vars=['var1','var2'], var_name='name_of_year_column_in_output', value_name='name_of_value_column_in_output')
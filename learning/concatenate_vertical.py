#concatenating DataFrames: pandas.concat() is used to vertically combine DataFrames, helpful for appending frows from one DataFrame to another
#   pd.concat() can concatenate both vertical & horizontal: axis=0, vertical (0 is the default so no need to explicity state it)

#if index value doesn't provide any useful info, can ignore index: pd.concat([col_1, col_2, col_3], ignore_index=True)
#setting labels to original tables: pd.concat([table1, table2, table3], ignore_index=False, keys=['col1', 'col2', 'col3'])
#concatenate tables with different column names: pd.concat([table1, table2], sort=True)     #if sort argument is true, it will alphabetically sort the different column names in the result
#if only matching columns between tables are wanted, set join="inner"

#verifying integrity of data: .merge(validate=None) -> checks if merge is of specified type such as 'one_to_one', 'one_to_many', 'many_to_one', 'many_to_many'
#we verify integrity b/c real world data is often not clean so verifying upfront saves us from having a mean skewed by duplicate values, or from creating inaccurate plots

#verifying concatentations: .concat(verify_integrity=False) checks whether the new concatenated index contains duplicates. Default value is False.
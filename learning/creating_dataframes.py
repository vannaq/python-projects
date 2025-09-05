#dictionary is a way of storing data in Python (reference dictionary.py)
#2 ways to create dataframes: from list of dictionaries (build row by row) & from a dictionary of lists (build column by column)
#list_of_dictionaries = [{"key":"value", "key1":"value1", "key2":"value2"}, {"1key":"1value", "2key1":"2alue1", "2key2":"2value2"}, {"3key":"3value", "3key1":"3value1"}...]
#dictionary of lists: each key is a column name, and each value is a list of column values
#dict_of_lists = {"key":["value1","value2"], "key2":["value_a","value_b"], "key": [2, 65] ...} --- note there's no quotes around integers

#convert list into dataframe: pd.DataFrame(list_name)
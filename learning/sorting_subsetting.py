#sort by column: dataframe.sort_values("column_name")
#sort in descending order: dataframe.sort_values("column_name", ascending=False)
#sort by multiple variables by passing a list of column names to sort_values: dataframe.sort_values(["column_name1", "column_name2"])
#sort by multiple variables and direction values are sorted in: dataframe.sort_values(["column_name1", "column_name2"], ascending=[True, False])

#subsetting rows is also known as filtering rows or selecting rows
#subsetting multiple columns: dataframe[["column1", "column2"]] where outer square brackets are subsetting the dataframe whereas inner square brackets are creating a list of column names to subset

#subsetting rows with boolean output: dataframe["column"] > 50
#subsetting rows with specific output: dataframe[dataframe["column"] > 50]
#subsetting rows based on dates: dataframe[dataframe["column"] < "2015-01-01"] 

#subsetting based on multiple conditions 
#is_lab = dogs["breed"] == "Labrador"
#is_brown = dogs["color"] == "Brown"
#dogs[is_lab & is_brown]
#subsetting based on multiple conditions as a one-liner: dogs[ (dogs["breed"] == "Labrador") & (dogs["color"] == "Brown")]

#subsetting using .isin() when you want to filter on multiple values of a categorical variable
#canu = ["California", "Arizona", "Nevada", "Utah"]
#mojave_homelessness = homelessness[homelessness["state"].isin(canu)]
#output is the filtered dataframe. Note that if the line is mojave_homelessness = homelessness["state"].isin(canu) then output is boolean series
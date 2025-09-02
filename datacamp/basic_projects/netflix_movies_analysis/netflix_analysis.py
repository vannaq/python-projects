#Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

#Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("datacamp/basic_projects/netflix_movies_analysis/netflix_data.csv", index_col=0)       #index_col=0 removes the indexing column


#Filter for Movies only
movies_only = netflix_df[netflix_df["type"] == "Movie"]


#Filter for Movies released between 1990 to 1999
movies_1990s = netflix_df[(netflix_df["release_year"] >= 1990) & (netflix_df["release_year"] < 2000)]


#Find most frequent movie duration in 1990s
duration = movies_1990s["duration"].mode().iloc[0]                                      #.mode() returns the most frequent value(s) in a column so if there's only one most frequent value, it'll return a series with 1 row. If there's a tie, it'll return multiple values. Without .iloc[0] the result will be two values where the first value is 0, which is the index of the series (not a value).
print(f"The most frequent movie duration in the 1990s was {duration} minutes.")


#Filter for short action movie genre, which is less than 90 minutes long
short_action_movie = movies_1990s[(movies_1990s["duration"] < 90) & (movies_1990s["genre"] == "Action")]

#Using len function, we can find the number of items in the filtered series from the previous step
short_movie_count = len(short_action_movie)
print(f"The number of short action movies released in 1990s is {short_movie_count}.")


# While the following section of code works, it is slow and more memory-intensive than vectorized pandas filtering.
#####
# Create an empty array 
# shorts = []

# #Iterate through all rows of the dataframe to find those with duration less than 60 and of the music genre 
# for index, row in netflix_df.iterrows():
#     if (row["duration"] < 70 and row["genre"] == "Music"):
#         shorts.append(row)                                  #add row to empty array created in previous step
# print(shorts)

#Convert series back into a dataframe
# shorts_df = pd.DataFrame(shorts)
######

#Boolean indexing to replace the above section of code is much faster & cleaner
shorts_df = netflix_df[(netflix_df["duration"] < 70) & (netflix_df["genre"] == "Music")]

#Export to csv and save to location 
shorts_df.to_csv('datacamp/basic_projects/netflix_movies_analysis/shorts.csv', index=False)

 



#problem #1: Which NYC schools have the best math results?
#the best math results are at least 80% of the "max possible score of 800" for math

#problem #2: What are the top 10 performing schools based on the combined SAT scores?

#problem #3: Which single borough has the largest standard deviation in the combined SAT score?

#import pandas
import pandas as pd

#read in the data
schools = pd.read_csv("datacamp/basic_projects/nyc_test_scores/schools.csv")

#preview data
#print(schools.head())

#1 create pandas DataFrame, filtering by school_name and average_math, sorted by average_math in descending order
sorted_math_schools = schools.loc[:, ["school_name","average_math"]].sort_values("average_math", ascending=False)

#subset sorted DataFrame to print best math results that are at least 80% of the max possible score of 800 for math
best_math_schools = sorted_math_schools[sorted_math_schools["average_math"] >= (.8 * 800)]

#print best_math_schools to verify results
print(best_math_schools.set_index("school_name"))



#2 to get top 10 performing schools based on combined SAT scores, first create pandas DataFrame with new column "total_SAT"
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
top_10_schools = schools[["school_name", "total_SAT"]].sort_values("total_SAT", ascending=False).head(10)
print(top_10_schools.reset_index(drop=True))


#to get largest std dev borough, first group data by borough and use .agg() to get counts, mean, std
borough_grouped = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)

#filter for largest stddev and then rename columns for clarity
large_std_dev = borough_grouped[borough_grouped["std"] == (borough_grouped["std"].max())]
largest_std_dev =  large_std_dev.rename(columns={"count":"num_schools", "mean":"average_SAT", "std":"std_SAT"})
print(largest_std_dev)

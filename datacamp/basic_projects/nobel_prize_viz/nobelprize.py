#Analyze NP winner data to answer 5 questions
#Q1. What is the most commonly awarded gender and birth country? (store answers in variables top_gender and top_country)
#Q2. Which decade had the highest ratio of US-born NP winners to total winners in all categories? (store answer as integer called max_decade_usa)
#Q3. Which decade and NP category combination had the highest proportion of female laureates? (store as dictionary called max_female_dict where decade is key, category is value)
#Q4. Who was the first woman to receive a NP, and in what category? (save string answers as first_woman_name and first_woman_category)
#Q5. Which individuals or organizations have won more than one NP throughout the years? (store full names in a list named repeat_list)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#bring in data
nobel = pd.read_csv("datacamp/basic_projects/nobel_prize_viz/nobel.csv")

#view all columns in dataset
# print(nobel.columns)

#use .value_counts() to get a Series containing counts of unique values in descending order
#use .index[0] to return top value
top_gender = nobel["sex"].value_counts().index[0]    
top_country = nobel["birth_country"].value_counts().index[0]

###Q1. print most commonly awarded gender and country
print("\nMost commonly awarded gender:",top_gender)
print("\nMost commonly awarded country:",top_country)


###Q2. create new Boolean column for US-born winners
nobel["us_born_winners"] = nobel["birth_country"] == "United States of America"

#now i have a year column and a boolean column for whether a country has US winner. i want to group the year into decades 
#create a decade column -> do integer division to get decades
nobel["decade"] = (nobel["year"] // 10) * 10

#then count number of US winners per decade
us_winners_per_decade = nobel.groupby("decade").sum()
# print(us_winners_per_decade)

#alternatively, can group rows by decade, select specific column to aggregate, count the Trues from Boolean column, then convert back to DataFrame
#us_winners_per_decade = nobel.groupby("decade")["us_born_winners"].sum().reset_index()

#now we have 13 rows grouped by decade and a count of number of us_born_winners per decade (new column at end of DataFrame)
#since decade is the index, use .idxmax() to return index of the max value for column us_born_winners
max_decade_usa = us_winners_per_decade["us_born_winners"].idxmax()
print("\nDecade with highest number of US-born winners:", max_decade_usa)

#alternatively, max_decade_usa = us_winners_per_decade.loc[us_winners_per_decade["us_born_winners"].idxmax(), "decade"]

#create relational line plot 
sns.relplot(x="decade", y="us_born_winners", data=us_winners_per_decade, kind="line")
plt.title("Number of US-born Nobel Prize Winners per Decade")
plt.xlabel("Decade")
plt.ylabel("Number of US-born Winners")
plt.show()

###Q3. group DataFrame by decade and category, then use .size() to count how many rows are in each group
grouped_decade_category = nobel.groupby(["decade", "category"]).size()

#filter for laureate_type = individuals
individual_laureates = nobel[nobel["laureate_type"] == "Individual"]

# find female laureates and group by decade and category, then count how many rows are in each group
total_female_laureates = individual_laureates[individual_laureates["sex"] == "Female"].groupby(["decade","category"]).size()

# find total laureates, count how many rows are in each group
total_laureates = nobel.groupby(["decade", "category"]).size()

#find proportion of female laureates
prop_female_laureates = total_female_laureates / total_laureates
# print(prop_female_laureates.index.names)  #check index names

#find the index, which is decade, category, of max proportion of female laureates
max_index = prop_female_laureates.idxmax()

# #create dictionary to store output
max_female_dict = {int(max_index[0]) : max_index[1]}
print("\n",max_female_dict)

# To plot US-born winners per decade by category, group by both 'decade' and 'category'
us_winners_per_decade_category = nobel[nobel["us_born_winners"]].groupby(["decade", "category"]).size().reset_index(name="us_born_winners")

# Now 'category' is present in the DataFrame, so we can use it for hue
sns.relplot(x="decade", y="us_born_winners", data=us_winners_per_decade_category, kind="line", hue="category")
plt.title("Number of US-born Nobel Prize Winners per Decade by Category")
plt.xlabel("Decade")
plt.ylabel("Number of US-born Winners")
plt.show()


##Q4. find first woman winner's full_name and category
first_woman = nobel["sex"] == "Female"              #find first female in Dataframe
first_woman_loc = nobel.loc[first_woman].iloc[0]    #filter Dataframe where condition is True & select first row from filtered DataFrame
first_woman_name = first_woman_loc["full_name"]
first_woman_category = first_woman_loc["category"]
print("\nFirst woman to win Nobel Prize is", first_woman_name, "in the category of", first_woman_category)


##Q5. individuals or orgs winning more than 1 NP throughtout the years, store full names in list named repeat_list
#find duplicate winners
multi_winners = nobel["full_name"].value_counts()
multi_winners = multi_winners[multi_winners > 1]
repeat_list = multi_winners.index.tolist()
print(repeat_list)

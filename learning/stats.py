#Field of stats: the practice & study of collecting and analyzing data
#Summary stats: a fact about or summary of some data, like an avg or count
#Stats can answer a lot of questions but not why in a lot of cases

#Types of stats: 
# Descriptive - describe and summarize data
# Inferential - use sample data to make inferences about a larger population

#Types of data (there's more, but these two are the focus at this juncture of Python learning)
# Numeric (Quantitative) 
#   Continuous (Measured) -- e.g. airplane speed, time spent waiting in line
#   Discrete (Counted) -- e.g. number of pets, number of packages shipped
# Categorical (Qualitative)
#   Nominal (Unordered) -- categories with no inherent ordering, e.g. married/unmarried, country of residence
#   Ordinal (Ordered) -- inherent order, e.g. survey question indicating degree to which you agree with a statement

#Typical measures of center: Mean, median, mode
#Right skewed data is when majority of data is on the left with a tail to the right (opposite for left skewed data)
#when data is skewed, mean/median are different where mean is pulled in direction of skew so it's lower than the median on the left-skewed data & higher than median on right skewed data --> better to use median in these cases

#measures of spread: 
# variance - measures the average distance from each data point to the data's mean
#   use np.var() with ddof argument = 1: np.var(df['column'], ddof=1)
#   without ddof=1, population variance is calcuated instead of sample variance

#to get summary stats all in one go, use .describe() method which gives count, mean, std, min, quartiles, max
#to get quartiles: np.quantile(data, [0, 0.25, 0.5, 0.75, 1])

##Sampling##
#.sample(n=1) method
#setting random seed for reproducibility: np.random.seed(#)
#sampling with replacement, set the replace argument to True: df.sample(seed, replace=True)
#to get counts: df.value_counts()

#Discrete distributions#
#discrete uniform distribution is when all outcomes have the same probability, like a fair die
#law of large numbers: as the size of sample increases, sample mean will approach theoretical mean
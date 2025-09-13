#Discrete distributions#
#discrete uniform distribution is when all outcomes have the same probability, like a fair die
#law of large numbers: as the size of sample increases, sample mean will approach theoretical mean

#uniform distribution
#from scipy.stats import uniform
#uniform.cdf(value, lower limit, upper limit)
##greater than probabilities: 1 - uniform(value, lower limit, upper limit)
##probabilities in between 2 values: uniform.cdf(upper value, LL, UL) - uniform.cdf(lower value, LL, UL)

##generating random numbers according to uniform distribution: uniform.rvs(min value, max value, size=random number of values to generate)


#binomial distributions#
#binomial distribution is a probability distribution of the number of successes in a sequence of independent trials
#from scipy.stats import binom
#random variates for generating random numbers from a distribution: binom.rvs(# of trials, probability of success, size=# of trials)
#probability mass function gives probability of a discrete random variable equalling a specific value:binom.pmf(# of successes, # of trials, probability of success)
#cumulative distribution function gives probability of a random variable being less than or equal to a value: binom.cdf(# of successes, # of trials, probability of success)
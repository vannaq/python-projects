#Discrete distributions#
#discrete uniform distribution is when all outcomes have the same probability, like a fair die
#law of large numbers: as the size of sample increases, sample mean will approach theoretical mean

#uniform distribution#
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
#cumulative distribution function for probability of greater than: 1 - binom.cdf(# of successes, # of trials, probability of success)
#expected value of a binomial distribution, which is avg # of successes over many trials, can be calculated by (# of successes * # of trials)


#normal distributions#
#answers "what is the cumulative probability up to a given value?": norm.cdf(# of interest, mean, std dev)
#answers "what value corresponds to a given cumulative probability?": norm.ppf(# of interest, mean, std dev)
#norm.rvs(mean, std dev, size=# of samples)


#poisson distribution#
#events appear to happen at a certain rate, but completely at random; e.g. # of people arriving at a restaurant/hr or # of animals adopted per week at shelter
#probability of some # of events occurring over a fixed period of time
#probability of a single value: poisson.pmf(# of interest, mean)
#probability of less than or equal to: poisson.cdf(# of interest, mean)
#probability of greater than: 1 - poisson.cdf()
#sampling: poisson.rvs(mean, size=# of simulations)


#exponential distributions#
#represents probability of time between Poisson events
#probability of less than: expon.cdf(# of interest, scale=lambda value)
#probability of greater than: 1-expon.cdf(# of interest, scale=lambda value)
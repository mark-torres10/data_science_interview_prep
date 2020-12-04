## Review of Statistics Terms

### Central Limit Theorem

Here's a great introduction to the CLT: https://spin.atomicobject.com/2015/02/12/central-limit-theorem-intro/

#### Formal definition
The central limit tells us that if we take samples from the population, the samples should be normally distributed, regardless of the distribution of the actual population.

If we take a bunch of samples, each with size "n", from a population with mean = pop_mean and variance = pop_var, then the distribution of the samples will tend towards a normal distribution, whose mean approximates pop_mean and whose variance is proportional to the number of samples per sample. 

Here's a great gif (from https://hawkeslearningblog.files.wordpress.com/2016/03/statistics-simulation.gif?w=665) that shows the CLT in action. On the left is the true population distribution, and on the right is the distribution of the means of the samples (with different plots for different values of "n", the sample size). 

![Simulation of Central Limit Theorem](https://hawkeslearningblog.files.wordpress.com/2016/03/statistics-simulation.gif?w=665)

If we look at, say, the distribution of means, what the CLT tells us is that if we take large enough samples (so, with large enough values for "n"), the mean of the means from the sample will converge (almost perfectly), as n approaches infinity, to the true population mean. Here's another great GIF that demonstrates that:

![Simulation of convergence of means with CLT](http://rex-analytics.com/wp-content/uploads/2016/06/www.LLN_.gif)

#### Practical examples

Example 1: Coin flips

For example, if you flip a coin 20 times, you might, on your first set of 20 tosses, get 15 heads and 5 tails, and in your second set of tosses, get 9 heads and 11 tails. If you do this over and over and track the number of heads that you get, what you'll see is a normal distribution centered around x = 10 heads. 

In another example, if we wanted to know the average height of people, we don't know how that's actually distributed in the population, so what we can do is take a bunch of samples of people, get their average height, and do that sampling over and over. If we record the means and plot the distribution of the means, the mean of that distribution should approximate the population mean. 

Essentially, if we take a bunch of samples, the mean of the means will approximate the true population mean 


### Law of Large Numbers


### What's the different between the Central Limit Theorem and the Law of Large Numbers?

These two ideas are frequently mixed up, and they both do deal with the behavior of the sample mean and asymptotics. Here's a great visual explaining the difference in the two:

![Difference between CLT and LLN](http://rex-analytics.com/wp-content/uploads/2016/06/CLT-vs-LLN.png)



### Expectation

### Covariance

### Variance

### Standard deviation


## Distributions

### Uniform distribution

#### Definition

#### Use cases

### Normal distribution

#### Definition

#### Use cases

### Binomial distribution

#### Definition

#### Use cases

### Geometric distribution

#### Definition

#### Use cases

## Bayesian Statistics

### Bayes Theorem

## Statistical Inference

### Maximum likelihood

### Univariate analysis

### Bivariate analysis

For bivariate analyses, we want to compare two inputs, X1 and X2. The way we do so depends on whether they're numeric, categorical, or some combination of the two, as well as the type of question that we'd like to answer

####
 
### Multivariate analysis

## Hypothesis Testing

### T-distributions

### Z-distributions

### t-test

### z-test

### p-values

### alpha

### beta

### Confidence interval 

### Standard error

### Margin of error

### Power

## End of Study Guide

 

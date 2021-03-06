## Review of Statistics Terms

### Basic Statistics

### Combinatorics (i.e., how to count)

Combinatorics is about either finding how many ways some objects can be chosen from a sample (e.g., how many ways can you pick 4 people from a room of 10 people?) or finding how many ways you can arrange some objects. 

#### Inclusion-Exclusion Principle

The inclusion-exclusion principle says that if you want to, for example, find P(A or B), then P(A or B) = P(A) + P(B) - P(A and B). If you add more events, then there are further generalizations (for example, P(A or B or C) = P(A) + P(B) + P(C) - P(A and B) - P(A and C) - P(B and C) + P(A and B and C)). 
##### Example Question: How many numbers between 1 and 1000, including both, are divisible by 3 or 4?

Number of numbers, between 1 and 1000, that are divisible by 3 = math.floor(1000 / 3) = 333
Number of numbers, between 1 and 1000, that are divisible by 4 = 1000 / 4 = 250
Number of numbers, between 1 and 1000, that are divisible by 3 and 4 = 1000 / (3 * 4) = 83

Answer = 333 + 250 - 83 = 500


### Central Limit Theorem

Here's a great introduction to the CLT: https://spin.atomicobject.com/2015/02/12/central-limit-theorem-intro/

#### Formal definition
The central limit tells us that if we take samples from the population, the samples should be normally distributed, regardless of the distribution of the actual population.

If we take a bunch of samples, each with size "n", from a population with mean = pop_mean and variance = pop_var, then the distribution of the samples will tend towards a normal distribution, whose mean approximates pop_mean and whose variance is proportional to the number of samples per sample. 

Here's a great gif (from https://hawkeslearningblog.files.wordpress.com/2016/03/statistics-simulation.gif?w=665) that shows the CLT in action. On the left is the true population distribution, and on the right is the distribution of the means of the samples (with different plots for different values of "n", the sample size). 

![Simulation of Central Limit Theorem](https://hawkeslearningblog.files.wordpress.com/2016/03/statistics-simulation.gif?w=665)

If we look at, say, the distribution of means, what the CLT tells us is that if we take large enough samples (so, with large enough values for "n"), the mean of the means from the sample will converge (almost perfectly), as n approaches infinity, to the true population mean. Here's another great GIF that demonstrates that:

![Simulation of convergence of means with CLT](http://rex-analytics.com/wp-content/uploads/2016/06/www.LLN_.gif)

We get the convergence in mean because, although the CLT doesn't tell us what the mean is going to be, we know that the sample means are going to be normally distributed, with a mean ~ population mean and variance ~ population variance / square root (n). Therefore, as "n", the sample size, increases, we get a distribution of the means that is narrower. 

Importantly, the CLT tells us information about the **distribution** of the samples (and, taken one step further, the means of the samples), and not necessarily what the actual value is. Why does this make a difference? If we're trying to estimate a value (e.g., a t-statistic), we have an estimate for the t-statistic, sure, but the CLT gives us the distribution of what possible values our t-statistic can take. Therefore, the CLT is useful for telling us the limit distributions of things like the t-statistic or parameters for our models. 

#### Practical examples

Example 1: Coin flips

For example, if you flip a coin 20 times, you might, on your first set of 20 tosses, get 15 heads and 5 tails, and in your second set of tosses, get 9 heads and 11 tails. If you do this over and over and track the number of heads that you get, what you'll see is a normal distribution centered around x = 10 heads. 

In another example, if we wanted to know the average height of people, we don't know how that's actually distributed in the population, so what we can do is take a bunch of samples of people, get their average height, and do that sampling over and over. If we record the means and plot the distribution of the means, the mean of that distribution should approximate the population mean. 

Essentially, if we take a bunch of samples, the mean of the means will approximate the true population mean 


### Law of Large Numbers

#### Formal definition

Here's a great explanation of the LLN: http://rex-analytics.com/the-law-of-large-numbers-its-not-the-central-limit-theorem/

The Law of Large Numbers (LLN) says that if you take a large enough sample then, no matter what the true distribution of the population is, the sample mean is going to converge to the population mean (so the sample mean of a large enough sample is going to be a consistent, unbiased estimator of the population mean). 

#### Practical example

Taking our coin example from before, instead of flipping a coin 20 times, recording the number of heads, and then doing that again and again, we can instead do it as one sample. 

In the CLT case, if we, say, take 100 samples of us flipping the coin 20 times, then the number of heads in each sample of 20 tosses, when plotted on a distribution, should be normally distribution with a mean around x = 10 and a variance of the population variance / square root of 20. 

In the LLN case, let's just do all 100 * 20, or 2000, tosses all at once (instead of in separate samples). Then, the number of heads that we get should be around 1000, which is what we'd expect from the population distribution. 

As you can see, the CLT and LLN can be used in similar ways, which can lead to some confusion about which to use in what case (more on that in the next part).  

### What's the different between the Central Limit Theorem and the Law of Large Numbers?

These two ideas are frequently mixed up, and they both do deal with the behavior of the sample mean and asymptotics. Here's a great visual explaining the difference in the two:

![Difference between CLT and LLN](http://rex-analytics.com/wp-content/uploads/2016/06/CLT-vs-LLN.png)

Namely, the CLT tells us what happens if we (1) take a bunch of samples and (2) record their mean, then (3) what is the distribution of those sample means. In contrast, the LLN tells us what happens if we (1) take one, really large sample, (2) record its mean, and then (3) compare that mean to the population mean. 

### Expectation

### Covariance

### Variance

### Standard deviation


## Distributions

### Uniform distribution

The PDF of the uniform distribution: 

![PDF of uniform distribution](https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Uniform_Distribution_PDF_SVG.svg/250px-Uniform_Distribution_PDF_SVG.svg.png)

The CDF of the uniform distribution:

![CDF of uniform distribution](https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Uniform_cdf.svg/250px-Uniform_cdf.svg.png)

#### Definition

The uniform distribution is a probability distribution, between two bounds "a" and "b", that say that every outcome in between "a" and "b" is equally likely. 

The equation for the uniform distribution is: 

![Equation of uniform distribution](https://wikimedia.org/api/rest_v1/media/math/render/svg/b701524dbfea89ed90316dbc48c5b62954d7411c)

#### Use cases

We can use the uniform distribution for (continuous) events where each outcome is equally likely. 

### Normal distribution

The PDF of the normal distribution is:

![PDF of the normal distribution](https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Normal_Distribution_PDF.svg/220px-Normal_Distribution_PDF.svg.png)

The CDF of the normal distribution is:

![CDF of the normal distribution](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Normal_Distribution_CDF.svg/220px-Normal_Distribution_CDF.svg.png)

#### Definition

The normal distribution is a probability distribution that's often used as the "default" distribution (largely because of the implications of the CLT (see above), which says that no matter what the actual distribution is, if we take large enough samples, the samples, in their aggregate, will be normally distributed). 

The standard equation for a normal distribution is: 

![Equation of normal distribution](https://wikimedia.org/api/rest_v1/media/math/render/svg/3123d8dd4c3386afe9fac119fed2cfaf7ce9f336)

#### Use cases

As stated above, the normal distribution is popular for many use cases, because of the implications of the CLT. Often, if you don't know what distribution might be appropriate, then the normal distribution is likely your best prior (and, also, many models/techniques depend on data being normally distributed). 

### Binomial distribution

#### Definition

#### Use cases

### Geometric distribution

#### Definition

#### Use cases

## Bayesian Statistics

### Bayes Theorem

Here's a really interesting GIF of Bayes' Theorem in action:

![GIF of Bayes' Theorem, as illustrated by dropping balls](https://steemitimages.com/DQmcEqtXLTjxgPAsnFjstxoFuFgxPJJh94MxnCbAUVjfC47/Bayes_theorem_visual.gif)


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



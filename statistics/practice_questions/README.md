# Statistics Practice Questions

## Combinatorics / counting questions

## Dice questions

### What is the most likely outcome if you roll two dice and take their sum?

Here are two ways to intuite the answer:

(1) Using statistics, we know that, in expectation, the mean outcome of a given die is 3.5. So, the mean outcome of two dice, since they're independent variables, is 3.5 + 3.5 = 7. 

(2) Using reasoning, we can reason that 7 should be the answer. Let's say that the answer is something above 7. Take 8 for example. If we roll a 1 on the first die, we already cannot get 8 as a sum. Therefore, for 8 and above, there's a possibility that, based off our first roll, we can't get the desired sum. If we take the numbers below 7, the same holds true. For example, if we want a sum of 6, then if we roll a 6 on the first die we already can't get 6 in total. The only sum where it's still possible to get that outcome regardless of what you roll on the first die is 7. 

### How would you determine if a die was unfair?

The standard approach would be to use a chi-squared test. You want to determine the degree of confidence that you'd like in your answers, and then use a chi-squared test to determine the number of rolls that you'd need to determine, with a certain degree of confidence, if the die was unfair. 

Source: https://math.stackexchange.com/questions/57624/how-many-rolls-do-i-need-to-determine-if-my-dice-are-fair

 
## Coin questions

### How would you determine if a coin was unfair?

You can use a binomial test (which is just using the binomial distribution formula): https://www.spss-tutorials.com/binomial-test/

Here's the equation for the binomial distribution:

![Equation for binomial distribution](https://www.onlinemathlearning.com/image-files/binomial-distribution-formula.png)

### If you have a biased coin, how could you simulate an unbiased coin?

From this link: https://medium.com/@hjegeorge/interview-question-1-a-biased-coin-toss-9dc2af96321

### There is a fair coin (one side heads, one side tails) and an unfair coin (both sides tails). You pick one at random, flip it 5 times, and observe that it comes up as tails all five times. What is the chance that you are flipping the unfair coin?

Source: https://www.nicksingh.com/posts/40-probability-statistics-data-science-interview-questions-asked-by-fang-wall-street

This involves Bayesian probability. 

What you want is P(Unfair | 5 tails), and to solve for that, what you can do is:

P(Unfair | 5 tails) = [P(5 tails | Unfair) * P(Unfair)] / P(5 tails).

P(5 tails) = P(5 tails | Fair)P(Fair) + P(5 tails | Unfair)P(Unfair)

Plugging these in, you get 32/33 as your answer, or about 97%. 

### What is the expected number of coin flips needed to get two consecutive heads?

Source: https://www.nicksingh.com/posts/40-probability-statistics-data-science-interview-questions-asked-by-fang-wall-street

Let X be the result of getting 2 heads. 

Let's say that you flip the coin once. Then:

E[X] = (1/2)(1 + E[X|H]) + (1/2)(1 + E[X|T])

We know that E[X|T] = E[X], since we'd just have to start over from scratch.

Now, let's solve for E[X|H]. Just like with E[X], let's split up E[X|H] into its two possible outcomes:

E[X|H] = (1/2)(1 + E[X|HH]) + (1/2)(1 + E[X|HT])

We know that E[X|HH] = 0 (we're done, we got two heads in a row), and we also know that E[X|HT] = E[X] (since we'd have to start from scratch. Plugging those into E[X|H], we get:

E[X|H] = (1/2)(1 + 0) + (1/2)(1 + E[X]) = 1 + (1/2)E[X]

Plugging E[X|H] into our equation for E[X]:

E[X] = (1/2)(1 + E[X|H]) + (1/2)(1 + E[X|T]). 

Now, let's plug in E[X|H] = 1 + (1/2)E[X] and E[X|T] = E[X]:

E[X] = (1/2)(1 + 1 + (1/2)E[X]) + (1/2)(1 + E[X]) = 1 + (1/4)E[X] + (1/2) + (1/2)E[X] = (3/2) + (3/4)E[X]

Now, we have the following:

E[X] = (3/2) + (3/4)E[X]

Solving for E[X], we get E[X] = 6

### A and B are playing a game where A has n+1 coins, B has n coins, and they each flip all of their coins. What is the probability that A will have more heads than B?

Source: https://www.nicksingh.com/posts/40-probability-statistics-data-science-interview-questions-asked-by-fang-wall-street

Let's start with what could happen after the first "n" tosses. After "n" tosses, there are 3 possibilities:

1. A has more heads than B
2. A and B have the same number of heads
3. A has less heads than B

In scenario 1, A will always win (since they've already got more heads than B) and in scenario 3, A will always lose (since even if they get heads on the next toss, they won't have more heads than B). By symmetry, P(Event 1) = P(Event 3). So, let's set X = P(Event 1) = P(Event 3). Now, let's set y = P(Event 2). Since these are the only three possible scenarios, we know that:

P(Event 1) + P(Event 2) + P(Event 3) = 1

X + Y + X = 1

2X + Y = 1

So, Y = 1-2X. 

Now, we know that in half of the times that Event 2 happens, A will win, since in half of the circumstances they'll get heads. As a result, the probability thatA wins is denoted by:

P(Event 1) + (1/2)P(Event 2) = X + (1/2)Y = X + (1/2)(1 - 2X) = X + 1/2 - X = 1/2

So, the probability that A wins is 1/2. 

###  A person flips an unbiased coin over and over again. Player A looks for the sequence HHT and player B looks for the sequence HTT. What is the probability that player A encounters their sequence first?

Source: https://towardsdatascience.com/12-probability-practice-questions-for-data-science-interviews-2ec5230304d9

Let's take event A as the event where we see HHT before HTT. 

So, let's toss the coin once and see what we get:

P(A) = (1/2)P(A|H) + (1/2)P(A|T)

Since a T on the first toss means that we can't get HHT or HTT, it's the equivalent of having to restart. Rewriting our equation, we get:

P(A) = (1/2)P(A|H) + (1/2)P(A) => (1/2)P(A) = (1/2)P(A|H), or P(A) = P(A|H). 

Now, we only have to solve for P(A|H). Let's do conditioning on the second toss now. 

P(A|H) = (1/2)P(A|HH) + (1/2)P(A|HT)

Let's take a look at P(A|HH):

If we have P(A|HH), then to get HHT you need 1 T while to get HTT you need 2 Ts. So, it's impossible to get HTT without getting HHT first. Therefore, P(A|HH) = 1. 

Now, let's take a look at P(A|HT):

P(A|HT) = (1/2)P(A|HTH) + (1/2)P(A|HTT). 

Looking at P(A|HTT), A already loses (since we see HTT before HHT), so P(A|HTT) = 0
Looking at P(A|HTH), this is the same as having to start over with one H, so P(A|HTH) = P(A|H). 

Therefore, P(A|HT) = (1/2)P(A|H) + 0

Now, plugging that into our equation above:

P(A|H) = (1/2)(1) + (1/2)( (1/2)P(A|H) ) = (1/2) + (1/4)P(A|H)

P(A|H) = (1/2) + (1/4)P(A|H) = P(A) ==> (3/4)P(A|H) = (1/2), or P(A|H) = 2/3 = P(A)

Therefore, the probability of seeing HHT before HTT is 2/3. 

###

## Card questions

## Probability questions

### Person A and Person B are playing archery together. Assume their abilities to fire the arrow at the target are exactly the same, and the probability of getting the target is 0.5 for both of them. Now that given A has fired 201 arrows and B has fired 200 arrows, what is the probability that A gets more targets than B?

From: https://towardsdatascience.com/12-probability-practice-questions-for-data-science-interviews-2ec5230304d9

### During flu season, for a two-parent heterosexual family, suppose the probability that at least one parent has the flu is 17%; the probability that the father has the flu is 12%; the probability that both the parents have the flu is 6%, what is the probability that the mother has flu?

From: https://towardsdatascience.com/12-probability-practice-questions-for-data-science-interviews-2ec5230304d9

### You have 40 cards in four colors, 10 reds, 10 greens, 10 blues, and ten yellows. Each color has a number from 1 to 10. When you pick two cards without replacement, what is the probability that the two cards are not in the same color and not in the same number?

From: https://towardsdatascience.com/12-probability-practice-questions-for-data-science-interviews-2ec5230304d9

## Conditional / Bayesian probability:

### (Part A): Mr. Jones has two children. The older child is a girl. What is the probability that both children are girls? (Part B): Mr. Smith has two children. At least one of them is a boy. What is the probability that both children are boys?

From: https://towardsdatascience.com/12-probability-practice-questions-for-data-science-interviews-2ec5230304d9

### You are given a choice of three doors by an Angel. You can choose only one of the doors among the three. Out of these three doors, two contain nothing and one has a jackpot. After you choose one of the doors, the angel reveals one of the other two doors behind which there is nothing. The angel gives you an opportunity to change the door or you can stick with your chosen door. You don’t know behind which door we have nothing. Should you switch or does it not matter?

From: https://towardsdatascience.com/12-probability-practice-questions-for-data-science-interviews-2ec5230304d9

### There are four boxes: A, B, C, D. John put a ball randomly in one of the four boxes and let David guess which box he put the ball. David guessed that the ball is in box A, but he was not sure. John gives him a hint that the ball is not in box B. At this time, what is the probability that the ball is in box C?

From: https://towardsdatascience.com/12-probability-practice-questions-for-data-science-interviews-2ec5230304d9

### Suppose that in the world exist a very rare disease. The chance for anyone to have this disease is 0.1%. You want to know whether you are infected so you go take a test, and the test results come positive. The accuracy of the test is 99%, meaning that 99% of the people who tested positive actually have the disease. What is the chance that you are actually infected?

From: https://towardsdatascience.com/12-probability-practice-questions-for-data-science-interviews-2ec5230304d9



## Pure statistics

### Say you are running a multiple linear regression and believe there are several predictors that are correlated. How will the results of the regression be affected if they are indeed correlated? How would you deal with this problem?

Source: https://www.nicksingh.com/posts/40-probability-statistics-data-science-interview-questions-asked-by-fang-wall-street





# Practice questions for Data Science / Machine Learning

## Questions about specific models

## Model evaluation

## Regressions

### What are the assumptions of linear regression?

Source: https://www.jmp.com/en_us/statistics-knowledge-portal/what-is-regression/simple-linear-regression-assumptions.html

The assumptions of linear regression are: 
1. The true relationship is linear. 
2. Errors are normally distributed
3. Errors are homoskedastic (i.e., the variance in errors doesn't change depending on the input)
4. The independent variables should be independent (and not exhibit multicollinearity). 

### What is the use of an F-Test?

The F-test tests whether any of the independent variables significantly affects the output variable y. 

Here's a slide that summarizes the purpose of an F-test

![Purpose of F-test](https://image.slidesharecdn.com/multipleregression-130320062840-phpapp02/95/multiple-regression-18-638.jpg?cb=1363760985)

### Why do we take the squared residuals and not the regular residuals?

The sum of residuals in a regression is always going to be equal to zero (source: https://www.statisticshowto.com/residual/), so that's why we take the squared sum of residuals. 

### How can you use hypothesis testing in linear regression?

Source: https://www.upgrad.com/blog/machine-learning-interview-questions-answers-ii/

We can check the p-value of any given independent variable and observe whether the variable is significant in the prediction of the dependent variable. 
### What is the use of regularization? What's the difference between L1 and L2 regularization?



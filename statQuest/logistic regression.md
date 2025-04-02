# Maximum Likelihood in Logistic Regression (Model Comparison)

## 1. Core Concept of Maximum Likelihood Estimation (MLE)
MLE finds the model parameters that **maximize the probability** of observing the actual data.

For logistic regression:
- We estimate coefficients (β) that make the predicted probabilities **most consistent** with the observed outcomes
- Unlike OLS (which minimizes squared errors), MLE maximizes the **log-likelihood function**

## 2. Likelihood Function for Logistic Regression
The joint probability of observing all outcomes:

```math
L(β) = \prod_{i=1}^n p_i^{y_i}(1-p_i)^{1-y_i}


LL(β) = \sum_{i=1}^n [y_i \log(p_i) + (1-y_i)\log(1-p_i)]


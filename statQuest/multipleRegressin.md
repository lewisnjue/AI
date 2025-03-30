## mulitple regressin in machien learning 

multiple regressin is an extenstion of simple linear regressin where two or more independent variables are used to predict a dependent variable. it helps understand how mulitple factors contribute to a target outomme 

**key assumptions of mulple regression**
for multiple regression to work well, these assumptions should hold: 
- linearity - te relationship between feature and target must be linear. 
- independence - feature should not be higly correlatd (avoid multicollinearity)
- homoscedansticity - residuls should have constant variace. 
- norality - residuals should be normally distributed. 

## why should we avoid multicollinearity in features ? 

multicollinearity occurs when two or more indepedent variables are higly correlated. while it does not direclty reduce a model predictive power, it causes instability in feature importance and interpretation. this can lead to misleading inshits and reduced model reliability. 


**key problems caused by multicollinearity**

1. unstable and unreliable coefficients 

- when two feature are highly correlated, the model struggles to determine which one actually influces the target. 
- this results in large flustuatins in coefficnet values when the data slighlty changes.


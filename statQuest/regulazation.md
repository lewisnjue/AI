## ridge regression

this model solves a regresion model where the loss funciton is the linear leat square funciton and regularization is givne by the l2-norm. alo known a redge regresionor tikhonov regularization. this estimator has built-in spport for mutlivariance regression ie shape of (n_samples,n_targets)

*key takeaways*

- adds an l2 penalty to shrink coefficeints and prevent overfitting. 
- does not eliminate feaature, inlike lasso.
- useful for multicollinear data and high dimensional problems. 


## lasso regression 

lasso regression is a type of linear regresion that adds an l1 regularization penalty to prevetn overfitting and perform feature seleciton by shrinking some coeficients exactly to zero. 

## elastic net regression 

elatic net regression is a hybird of ridge and laso regression, combining boh l1 and l2 regularization to improve performance in high-demenstinal datasets especially when there are correlatied features. 


**why do we need elastic net**

while ridge and lasso both help prevent overfitting.

- lasso eliminate soem feature by settign coefficinet to exactly zero. but it struggles when feature are higly corrleated.
- ridge shrinkd cofficient byut nover set them to zero making it unsuitable for feature seleciotn 

**problem**
- laso alone many randomly drop one of two higly corrlated feaatures. 
- ridge alone keeps all feature even if some are redundant

solution? -> elastic ne combines both! 

you can look at the mathematics behind it 


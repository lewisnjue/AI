## saturated model in machine learning 

a saturated model is a model that has enought parameters to perfecly fi the training data. this mean hat: 
- the model has zero training error 
- it completely memorizes teh dataset instead of generalizing 
- it is higly prone to overfitting meaning it may not perform well on unseen data. 


**example of a saturated model**

- in linear regression , if you have n datapoints and you fit a ploynomial of degree n-1 , the model will pass exactly throught all points . this means here is no raining error, but it to flexible. and the model will o genralize well. 

- in deep  learin g, an overly complex neural network with too may layers and neurons can fit noise in the data . instead of learning acutal patterns  


*how to avoid saturation?*
- regularizaton (l1/l2,dropout,weight decay)
- reducing the model complexity (using fewer parameter)
- more trainin data to prevent memorization. 


## deviance in machine learning 

deviance i a statistial meaure of how well a model fit the data, commoly used in generelized linear models like logistic regression. it is similar to the concept of variance explained in regresion models. 

*mathematical defination*
deviance is defined as: 

D = -2 *(log likehook of the model = log likehood of the aturated model)

where: 
- log likehood of the model repreent how well the current fit the data. 
- log likehodd of the saturated model repreent the bet possibe fit (zero training error)

a lowe deviance means a good model fi, while a high deviance suggest poor fit. 


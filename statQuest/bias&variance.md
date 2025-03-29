## bias and vriance in machine leanring 
bias and variance are two key sources of error in a machine leanring model, affecting its ability to generalize to unseen data. nderstanding their tradeoff is crucial for buildin ga well performing model. 

*bias*
bias refers to the error introduces by approximating a real-world problem with a simplifed model. a model with high bis makes strong assumptions abou the data , leding to underfitting. 

*characteristics of high bias*
- the model is too simple and does not capture the underlying pattenrs 
- low traning accuray and low test accuray
- exmple: a liner regression model used for high non-liner data. 

*exampe of high bias*
if you use a liner model to fit a complex, curved dataset, it will fail to capture the relationship, leading to high training and tet errors.

*variance*
variance refers to the models sensitvity to small fluctuations in the training data. a model with high varince is overly complex and lerns noise instead fo the actual pattern, leding to overfitting. 

*characteristis of high variance*
- the model performs well on training data but pooly on test data. 
- the model is too flexible and caputres random noise. 
- example: a deep neurl netwr with too many parametres traine don small datset. 

*example of high variance:*
if you fit a high-degree polynomail regression to simple data, the model will caputre noise and wont generaize well to new data. 

the ideal model should balnce bias and variance to achieve good generalation 

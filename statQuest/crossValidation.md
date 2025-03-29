## cross validation
- cross validtion allows us to compare different machine leanring methods nd get a sense of how well they will wor in practice. 
- cross-validation is a sttistical technique used to evaluate the performance and generaliztin ability of a machine lenring model. it helps in assessing how well a model trained on a dataset will perform on unseen data. the main goal is to prevetn overfitting. (when the model performs well on traning dat but poorly on new dta) and to ensure robustness. 

**why use cross-validation?**
- trditional trin-test splits can lead to high variance in performance evalution if the split is not representtive. 
- cross-validtion provides a more reliable estimate of model performance by averaging results over multiple splits. 

**common types of cross-validation**
1. K-Fold cross-validation
- the dataset is divided into k equal -sized folds
- the model is traind on k-1 folds nd validated on the remiling 1 fold 
- this process is repeated k times, with ech fold serving as the validation set once. 
- the finl performcne is the average of all k runs. 
2. stratified k-Fold crosss validation 
- ensure ech fold has the sme proportion of target classes (useful for imbalnced datasets).

3. Leave one out corss validation 
-  a special cse of k-fold where k = number of samples
- each sample is used once as a validation set . 
- computatioally expensive but useful for small datasets. 

4. train-vlidtion-test split
- a simpler approach wheere data is split into training, validation and test sets. 

## example k-fold cross validation using scikit-learn

lets implement 5 fold cross validation on a simple regression problem using sklern. 

```py
import numpy as np 
from sklearn.model_selection import KFold,cross_val_score
from sklearn.linear_model import LinearRegression 
from sklern.dtasets import make_regression 

X,y = make_regression(n_samples=100,n_features=5,noise=0.1,random_state=42)
model = LinearRegresson()

# use 5 fold cross validation 
kfold = KFold(n_splite=5,shuffle=True,random_state=42)

# ealute the model suing cross validation 

scores = cross_val_score(model,X,y,cv=kfold,scoring='rs') # R^2 score 
print("cross-validation scores:",scores)
print("mean R^2 score:",np.mean(scorers))


```

## understaind the r^2 (r-squared ) metric for model evaluation 
the r^2 metric, also known as the coefficient of determination, is a statistical measure used to evaluate the performnce of regressin models. it indecates how wel the model expalins the variance in the target variable compared to a simple baseline model(usually the mean of the target)

**what does r2 represent?**
- r2 measures the proportion of variance in the depenent variable(y) that is predictbl from the independent variables(x).
- it ranges form -inf to 1. 
- 1 perfect fit 
- 0 model performs s badly as ust preidctint he mean of y. 
- negtive model perofrms worse that the mean baseline.

*mathematical formula*
r^2 = 1 - (sumofsqured residuals(SSR))/(totalsum of squres (SST))

*example in sklearn*
```py
from sklearn.metrics import r2_score 
import numpy as np 

y_true = np.array([3,5,9,9])
y_pred = np.array([2.8,5.1,7.2,8.9])

r2 = r2_score(y_true,y_pred)

print("r2 score:",r2)

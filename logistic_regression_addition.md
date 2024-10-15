in scitlearn , you can use the log los  fuction also called- entrolpy loss  to evaluate a classification model perfomance . 
cross entrolpy measres the distance between the predicted probability distribution and the actual labels . 

here how you can use log_loss in scikit-learn to evaluate you model 


example 

```py 

from sklearn.datasets import make_classifacaion 

from sklearn.linear_model import LogisticRegrssion 

from sklearn.model_selection import train_test_split 
from sklearn.metrics import log_loss

# stp 2 generate a dataset 

# Generate a random binary classification dataset
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# step3 train a logistic resgrsion model 

# Train a logistic regression model
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# step 4 predict probaibiles 

# Get the predicted probabilities for the test set
y_pred_proba = model.predict_proba(X_test)

# step 5 calcuate log loss ( cross -entropy)

# Calculate the cross-entropy loss (log loss)
loss = log_loss(y_test, y_pred_proba)
print(f'Log Loss: {loss}')

# output example 

Log Loss: 0.4582

```

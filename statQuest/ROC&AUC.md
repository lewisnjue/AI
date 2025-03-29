## ROC nd AUC in machine learning 
in classifiction problems , especilly fo imbalanced dataset, simple accuray is not always a reliable metric, this is where ROC (recive operating characteristic) curve and AUC(area under the curve) come into play. 


**ROC CURVE**
the roc curve is a graphical representation that shows the trdeoff between true positive and false postive rate. for different classification thresholds. 

*key metrcis*
true postive rate / sensitivity/ recall 

TPR = TP / (TP + FN)

(how much acutal postiives where correctly predicted ? )

false postiive rate (FPR)

FPR = FP / (FP + TN)

(how many actual negatives where incorrectly predicted as positive?)


*how it works:*
- a classifier produces a probability score.
- by changin gthe decision threshold we get different tpr and fpr values 
- the roc curve plots tpr vs fpr for all possible thresholds. 

**auc**
- auc represent the area under the roc curve. 
- it quantifies how well a model can distiguish between classes. 

example 
lets demostrate roc and auc using a classificaion model 

```py 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc, RocCurveDisplay

# Generate a binary classification dataset
X, y = make_classification(n_samples=500, n_features=10, random_state=42)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Random Forest classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Get predicted probabilities
y_probs = model.predict_proba(X_test)[:, 1]  # Probabilities for class 1

# Compute ROC curve
fpr, tpr, _ = roc_curve(y_test, y_probs)

# Compute AUC score
roc_auc = auc(fpr, tpr)

# Plot ROC Curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', lw=2, label=f'ROC Curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')  # Random model
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.title('ROC Curve')
plt.legend()
plt.show()

```

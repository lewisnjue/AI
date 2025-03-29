## confustion matric in machine learning 
a confusitn matrix is a performance evalutin metric used for classification models. it helps visulize how well a model distishishes between different classes. 

**metrics derived from confusion matrix**
from the confustin matrix, we can cacluate key classification metrics: 
- accuray = TP + TN / (TP+TN+FP+FN)
- precision = TP/(TP+FP) (how many predicted positives wer actually correct?) => this is sensitivity 
- recall(sensitivity) = TP/(TP+FN) (how many acutl postives were correctly predicted?)
- specificity = TN / (TN + FP)
- f-score: harmonic mean of precision and recall. 
exmple using sklearn 

lets implemtn a confusiton matrix using sklern with a simple classificaion model.

```py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# Generate synthetic binary classification data
X, y = make_classification(n_samples=500, n_features=10, random_state=42)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)


# Compute confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Display confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap="Blues")
plt.show()

print("Classification Report:\n", classification_report(y_test, y_pred))

```

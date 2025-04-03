## linear discriminant analyis in machine learning 

linear discriminant analysis is a supervied dimenionality redcution technique that finds a lower-dimensional space where class separability is maximized. 

unlike pca, which finds directions of maximum variance, lda fidns directios that best separate different classes. 

lda is used for both classificaiton and dimenionality reduciton. 

you can look at the math behind it 
example 

```py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply LDA (reduce to 2D)
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X_scaled, y)

# Plot LDA-transformed data
plt.scatter(X_lda[:, 0], X_lda[:, 1], c=y, cmap='viridis', alpha=0.7)
plt.xlabel('LDA Component 1')
plt.ylabel('LDA Component 2')
plt.title('LDA on Iris Dataset')
plt.show()
```

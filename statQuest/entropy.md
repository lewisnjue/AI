## entropy in machine learning and data science 

entropy is a key concept in information theory and widely used in machine learning, especially in decision trees and feature selection. it measues the uncertintly and impurity in a dataset. 

**what is entropy?**
entropy quntiies the degree of disorder or randomness in a dataset. in machine leanring, it tells us how mixed the data is in terms of class labels. 

H(x)  = - summation(pilogpi)

where 
H(x) = entropy
pi = probability of class i 
- the summation runs over all possible classes. 

*intuition*
- high entropy(~1): the dataset is high mixed (uncertain)
- low entropy(!0): the dataset is pure(low uncertinty)

## entropy in decision trees(inforation gain)

entropy is used to determine the best feature to split a dataset in decision trees. 
- information gain(IG) measures how much uncertaintly is reduced after a split. 

*intuation*
- a feature with high inforation gain is preferred for splitting 
- the decision tree continoues splitting untill entrpy is minimized. 


**python exampe: computing entorpy**
lets compute entropy for  dataset. 

```py
import numpy as np
from scipy.stats import entropy

def compute_entropy(y):
    # Get class probabilities
    values, counts = np.unique(y, return_counts=True)
    probabilities = counts / counts.sum()
    return entropy(probabilities, base=2)  # Base 2 for log_2

# Case 1: Pure dataset (all same class)
y_pure = ['Yes', 'Yes', 'Yes', 'Yes']
print("Entropy (Pure Dataset):", compute_entropy(y_pure))  # Output: 0

# Case 2: Mixed dataset (50-50)
y_mixed = ['Yes', 'No', 'Yes', 'No']
print("Entropy (Mixed Dataset):", compute_entropy(y_mixed))  # Output: 1

# Case 3: Skewed dataset (80-20)
y_skewed = ['Yes', 'Yes', 'Yes', 'No', 'Yes']
print("Entropy (Skewed Dataset):", compute_entropy(y_skewed))  # Output: <1

```
*key takeaways*
- entropy measures uncertainty -> higher entropy=more randomness. 
- used in decision trees -> helps decide which feature to split on. 
- lower entropy is desireble -> means a dataset is wel 0rganied. 


## PRINCIPLA COMPONENT ANALYIS(PCA)

principal compoent analysis is a dimensionality reduction technique used in machine learning to: 

- reduce the number of feature while retaining important informatin. 
- remove redundancy from corrated feature. 
- improve computational efficiency for high-dimensional data. 
- help visualize complex data in 2D or 3D . 

PCA transforms the data into a new coordinate system where the most important pattenr are captured in a few new feature called principal components. 

**intuaion behind PCA**
imagin you have a dataset with many correlated variables . PCA finds new axe (principal component) that: 

- capture teh maximum variance in the data. 
- are uncorrlated (orthogonal to each other)
- allow you to represent the data with fewere dimenstions while keeping most of the information. 


**how pca works**

- pca is affected by scale, so we standardize each feature to have a mean of 0 and variance of 1. 

X = X - MEAN/ STD 

- compute the covariance matrix 

the covariance matrix caputre relationships between variables. if variable are higly correlatd, PCA combine them itno fewer dimenstions. 

C = 1/m(X(t)X)


- compute eigenvalue and eighenvectors
eignevaleus meaure the amoutn of variance caputed by each principal component. 
- eigenvectors represent the directiosn of the principal component. 

larger eigenvalues mean the component caputes more variance.


- select top k principal components

we keep only top k component that capute the most variance. 
Xpca = X.Wk 

where Wk contains teh eignevectors of the top k components. 


- transofrm data to lower dimenstions. 


we project hte data onto the nw axes principal componen. this gives us a lower-deimnstional representaion of the original data. 

example of pca in python 

```py 

import numpy as np 

import matpotlib.pyplot as plt 

from sklearn.decomposition import PCA

from sklearn.preprocesing import StandrdScaler

from sklearn.dataset import load_iris 

# load dataset 
iris = load_iris()

X = iris.data


scaler = StandardScaler() 

X_scaled = slacer.fit_transform(X)

# apply PCA  reduce to 2 dimenstions 


pca = PCA(n_components=2)

X_pca = pca.fit_trasform(X_scaled)


# plot the transformed data 

plt.scaer(X_pca[:,0],X_pca[:,1],c=iris.target,cmap='viridis'alpha=0.7)

plt.xlabel('principal component 1')
plt.ylabel('principal componet 2')
plt.title('pca on iris dataset')
plt.show() 

```



## pca vs umap 

theya re not similar umap(uniform manifold approximaion and projection) are fundamentaly differnt in how they reduce dimenion, even though both hel in visualizization the sigpliyfng high-dimenstional data. 

*core concept*
- pca is a inear (dimeninality reduction) while umap i non-linear dimenstinaliy reduciton 
- pca finds new axes (principal component) that maximize variance while umap learn a graph-based manifold to preseve local and global structure. 
- pca uses eigen decomposition on the covariance marix while umap use k-nearest neigbour and graph-based learnng. 

and also umap caputre non-linear relationhip unlike pca. 

*intuition*

- pca finds stragiht-line directiosn that capute variance , like flattening a spere onto a plane. 

- umap learn how data point are connected and tries to preerve that structure in a lower dimenstion. 



*when should you use pca vs umap?*

use pca when: 
- you need interpretability 
- you are working with linear relatinhipes (features are correlated)
- you want to reduce dimensins before feeding data into ml model 

use umap when: 

- you want to visualize high-dimensinal data while preserving clusers and relatioships. 

- your data is complex, non-linar structreus eg images, genomics word embeddings

- you are woring on clusering problems eg umap often helps improve clustering performance. 

example 

```py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import umap
from sklearn.datasets import load_digits

# Load a high-dimensional dataset (handwritten digits, 64 features)
digits = load_digits()
X = digits.data
y = digits.target

# Apply PCA (reduce to 2D)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Apply UMAP (reduce to 2D)
umap_model = umap.UMAP(n_components=2, random_state=42)
X_umap = umap_model.fit_transform(X)

# Plot PCA
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', alpha=0.7)
plt.title('PCA on Digits Dataset')

# Plot UMAP
plt.subplot(1, 2, 2)
plt.scatter(X_umap[:, 0], X_umap[:, 1], c=y, cmap='viridis', alpha=0.7)
plt.title('UMAP on Digits Dataset')

plt.show()
```

## R^2 in machine learning 

r^2,or the coefficeint of determination, mearue how well a regression model fit the data. it tells you what percentage of the variance in hte depenednet variable(target) i explained by the independent variables(features)

R^2 = 1 - SSre / SStot 

where:
SSres = Sum of squared resuduals 
SStot  = total sum of squared (vairiance of actual vaue from their mean )
*limitations*
- a high r2 does not mean the model is good; it might be overitting. 
- a low r2 doest alwasy mean a bad model (especially n case with high noise).
- it does not measure causation, only correlation. 

## P-Value 

a p-value is used in hypothesis testing to determine the statistical sifngificance of a feature in regression models. it tells us whether a variable has a meaningful relationship with the target variable.

*interpretation*:
- lwo p-values (<0.05): the faeture is statistically signficant (strong evident aganisth the null hypothesis)
- high p-valuse (>0.05): the features is not statistically significant (weak evidence aganist the null hypothesis, measnign it might not be useful for prediction)

**how it is used in ML**
- in linear regression, the p-value helps determine whether to keep or remove a feature 
- in feature seleciton, p-values help identify which feature contribute most to the model.


*limitations*
- a low p-values does not imply a feature is practically important; it could just be statistically significatn due to a large dataset. 
- if many feature are tested, multiple testing issues may lead to false postives 


**p-values vs mutual inforamtin for feature selection**

1. p-values (statistical significance)

- comes from ypothesis testing 
- measures whether a feature has a statistically signifacnt relationhisp with teh target. 
- works well for linear relationships. 
- assumes normalty in dat and can be misleding with hgily correlated features. 

2. mutual inforamtion (informatin gain)

- measure the amount of information one variable provide about antoher.
- caputes non-linear relationhps unlike p-values 
- work well for both classification and regrsssion taks. 
- does not assume andy speciific distributon of the data. 


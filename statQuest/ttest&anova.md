## T-Test and ANOVA in machine learning 

BOth T-Test and Anova (anlyis of variance) are statistical methods used in machine learning for feature selection and hypothesis testing. they help determine whether a feature has a signiicant effect on the target variable. 


### T-Test in machine learning 
A t-test is used to compare the mean of two groups and check whether the difference is statistically significant. 


**types of t-tests**
1. independent t-test(unpaired t-test)
- compares the means of two independent groups 
- example: checking if male and female customer spend differently in online store. 

2. paired t-test 
- compares the mean of two related groups (before and after scenarios)
- example: checking if custoemr spending chagne before and after discount. 


t -test formult 

t = x1 -x2 / (sqrt(s1^2/n1 + s2^2/n2))


where x1 , x1 = mean of the two groups 

s1^2 , s2^2 = variance of the two groups 
n1,n2 = sample sizes of each group. 

*how ti used in machien learnign?*
- feature selection - help determine whetehr a categorical feature significalnty affects the target variable.
- ab testign - compares perforamance between two different models or groups. 
- checking model assumptions - verifes normality and equal variance before applying linear models. 


### ANOVA in machine learnign 
anova is a statistical test that compares teh eman of three or more groups to determine if at lest one group is signficanty different from the otehrs. 


*types of anova*
1. one-way anova
- compares one independent categorical variables across multiple groups. 
- example: comparing custoerm spending across different ages groups. 

2. two way anova
- compares the effect of two independent categorical variables on a depenent variable. 
- example: checking how both age and gender impact spending behavour. 


*how its used in machine learning?*
- feature seleciton - helps determine whether categorical features significantly mpact the target varible. 
- experimental analysis - compare different model setting or hyperparameters. 
- multiple-class classification problems - identiier if different categories affect the outcome differently. 


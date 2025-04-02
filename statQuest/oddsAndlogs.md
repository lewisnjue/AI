odds and logs-odds are fundamental concept inprobabilistic models, especially in logistic regrssion and classificaiton taks. they bridge teh gap between probabilites and linear models in trasforming bunded probabilites (0 to 1) into unbounded valeus (-inf to +inf)

**odds**

- odds represent the raion of the probability of an event occuring to the probabiity of it not occuring. 

odds = p / 1-p 

where p is the probability of the event.


**log-odds**

log-odds is teh natural logaritm of the odds.

log-odds = log(p/1-p)

also the ligit fuction.


*key properties*

- rage form -inf to +inf 
- symeetry logit(p) = -logit(1-p)

## why use log-odds in machine learning? 

a) linear modeling 
- probabilies(p) are bounded beween 0 and 1 , but linear modesl eg logistic regrssion predict unbounded values.

- solution: model log-odds as linear combination of features:

log(p/1-p) = b0 + b1x1 + ... + bnxn 

this is the logistic regrssion equation. 

b) numerical stabilty
- log-odds avoid division by zero when p = 0 or p =1.

c) interopretabilty 
- coefficients(bi) in logistic regrssin describe how feaure affect the log-odds of the outcome. 


**from log-odds o probability**

the invert os the logit fucntion is he sigmoid(logistic fucntion)

p = 1 / 1+ e^(-log-odds)
this convert model prediction batch to probabites. 

example: 
if a logistic regrssion predicts log-odds = 1.386 
p = 1 / 1 + e^(-1.386) = 0.8 


log-odds and logits are essentially the same concept, but hey are used in slightly different contexts (statitics vs deep learning). here isa clear breakdown.


both represetn teh unbounded, pre-activatio output of a model before being squashed into a probability via the logistic/sigmod funciton. 

mathematically the are identical 

logits = log(p/1-p)

where p is teh probabilty of the postive classs.

when you are converting to probabily in log-odds you will use sigmoid but for logits in deep learning you will use sigmoid for binary or sofamx(muli-class ) and i hope you know what we do in softmax .

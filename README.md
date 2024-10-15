# AI
## TYPES OF ARTIFICAIL INTELLIGENCE 
- artificial narrow intelligence 
- artifiacial general intelligence 
- artifiacial super intelligence

some of the sub branches here are : 
- machine learning -( is a subset of artifiacial intelligence that allows computers 
to learn from data and imporve their perfomance on a specific task without being explicitly 
programmed . intead of being given specific rules , machine learning 
algorithms identify pattersn and rleationships within data to make prediction or decisons)
- key compnents of machine learning : 
    - data : the foundation of mahcine learning its the information used to train the algoritms 
    - algorithm: the output of the learning process, which can be used to make predictions or 
    decisons . 

### TYPES OF MACHINE LEARNING 
1 supervesed learning : the algorithm is trained on a dataset with labed examples 
(input and output pairs) . the goal is to learn a mapping fuction that can predict outputs for a new unseen inputs . 
example : regrsssion and classification 
1 unsepervised learning: the algoritm is trained on a dataset without labels. the 
goal is to find patterns or structure wihtin the data . 
example clusterring and dimetntinality reduction 
1 reiforcement learning : the algorithm learns by interacting with an enviroment . 
it receives rewards or penalites based on its action and aims to mazimize its cumulative rewards 
examples : game playing , robotics . 


## DEEP LEARNING : 
deep learning is a subfiled of machine learning that focues on using artificail neurl networks with 
multiple layers to learn cmplex patterns in data . these neurla networks are 
inspired by the structure and fuction of the human brain 
## WHAT IS AI ? 
teh thory and developmen of computer systems able to perform tasks normally requireing human iterlligence such as visual perception , speech recognition, decison making and tranlation between languages 

## TYPES OF AI 

### artivicial narrow intelligence : 

artificial narrow intelligence also know as weak ai involoves applying ai only to specific taks 
## artificial general intelligence : 

artifical general intelligence also know as strong ai , ivolves 
machines that possess teh ability to perfomr any intellectaul task that a human can . 

## artificail super intelligence : 
is a term referring to the time when the capability of computers will supass humans 

## ALORITHM: 
a set of rules and statistical techniues used to learn patterns from data . 
## MODEL : 

a modle is trianed by using a machine learning algoritm . 

## PREDICTOR VAIRIABLE 

it is a feature of the data that can beused to predict the output 

## RESPONSE VARIABLE : 
it is teh feature or the output variable that needs to be predicted by using th predictor varaibles 

## TRAINING DATA  
the machine learning modle is built using the training data . 

## TESTING DATA 
the machine leanring model is evaluted usint the tesint data 

## MACHINE LEARNING PROCESS 

the machine learning process invlolve building  a predictive modle that can be used to find a solution for a problem statment 

## MACHINE LEARNING PROBLEMS 

### REGRESSION 
- supervised learnin g
- ouput is a contious quantity 
- main aim is to forecast or predict 
- eg predict stoack marke price 
- algorithm lenear regression 

### CLASSIFICATION 

- supervised learning 
- output is a categorical quanity 
- main aim is to compute the categoriy of the data 
- eg classfy emails as spam or non-spam 
- algorithm logistic regression 

### CLUSTERING 
- unsupervised learning 
- assigns data points into clusters 
- main aim is to group similar items clusters 
- eg find all transaction which are floudulent in nature 
- algorimt K-means 

## SUPERVISED LEARNING ALGORITHMS 
- linear regression 
- logistic regression 
- decision tree 
- random forest 
- naive bayes classifier 
- k nearest naighores 
- support vector mahcines 


## LINEAR REGRESSION 

linear regression is a method to predict dependent vairable based on values of independent varaibles . it can be used for the cases where we want to predict some continous quanity . 
- DEPENDENT VARAIBLE (Y):
the response variable whos value needs to be predcited. 
- INDEPENDENT VALIABLE(X):
the predictor varaile used to predict the response varaible 


## LOGISTIC REGRESSION 
logistic regresssion is a method used to predict a dependent variable, given a set of independent variables , such that the depenent varaibles is catagorical . 

## DECISION TREE 


## SEARCH ALGORITHM 


lets start at looking at some terminology 

- AGENT - >  entity that perceives its enviroment and acts upon that enviroment . 

- STATE -> a configuration of the agent and its enviroment . 

- INITIAL STATE -> the state in which the agent begins . 
- ACTIONS -> choices that can be made in state .

actions(s) returns the st og actions that can be executed in state s . 

- TRANSISON MODEL -> a description of what state results from performing any applicable action in any state. 

result(s,a) returns the state resulting from performing actions a in state s. 

- STATE SPACE -> the set of all states reachable from the initial state by any sequence of actions . 

- GOAL TEST -> way to determine whether a given state is a goal state . 

- PATH COST -> numerical const accocaited with a given path . 

a search problmes have the following 

- inital state 
- actions 
- transisiton model 
- goal test 
- path const function 

solution -> a sequence of actions that leads from the initail stat e to a goal state . 

optimal solution ->  a solution that ahs the lowest path cost among all solutions . 

## NODE 
a node is a data structure that keeps track of : 
- a state . 
- a parent ( node that generated this node)
- an action ( action applied to parent to get node)
- a path const ( frominitaila state to node )

## APPROACH 

- start with a frontier that contains the initial state. 
- repeat : 
    - if the frontier is empty , then no solution 
    - remove a node from the frontier . 
    - if node contains goal state, return the solution . 
    - expand node , add resulting nodes to the frontier 

## REVISED APPROACH 

- start with a frontier that continas the initial state. 
- start with an empty explored set . 
- REPEAT: 
    - if the frontier is empty , then no solution . 
    - remove a node from the frontier . 
    - if node contins goal state , return the solution 
    - add the node to the exproled set , 
    - expand node , add resuting ndoes to the frontier if they arent aleready in th frontier or the explored set , 


## REVOVING A NODE IN THE FRONTIER : 

there are diffrent ways to remove a node from the frontier one of themis : 
- stack : LAST IN FIRS OUT DATA TYPE ,
this version of algoritm is called depth first search , please dont forget that 

depth first search is a search algortm that always expands the deepest neod in the frontier . 

another seach algorith is called breadth first search 

this search algorithm that always expandas the shallwest node in the frontier  . 

- queue is used in breath first search , first in first out data type . 

## UNINFORMED SEARCH 

search strategy that uses no problme specific knowledge . 

## INFORMED SEARCH 

search straregy that uses problem specific knowledge to find solutions more efeciently . 

### GREEDY BEST FIRST SEARCH 

search algorithm that expands the node that is closest tot he goal, as estimated by a heuristic fuction h(n)


### A * SEARCH 

search algorithm that expands node with lowest valeu of g(n) + h(n)

g(n) = cost of reach node 

h(n) = estimated cost to goal 

a * search is optimal if : 
- h(n) is admissible ( never overestimates teh true cost ) and 

- h(n) is consistent ( for every node n and succeossor n  with sept cosnt c, h(n)<= h(npatent) + c)


## MINMAX ALGORITHM 

MAX(X) amis to mazimize score. 
MIN(O) aimst o minimize score . 



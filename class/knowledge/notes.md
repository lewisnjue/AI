if it dint rain, harry visited hagrid today.
harry visited hagrid or dumbledore today. but not both.

harry visted dumbledore today. 


based on this information we can conclude:

Harry did not visit Hagrid today. 

It rained today. 

this is based on the knowledge. 

this is logical reason enable use to do so . 

**sentence**
an assertion about the word in a knowledge representation language..

**propasitional logic**

*proposition sysmplos*
p q r -> represent the sentences or fact about the world. 

*logical connectives*
- not ~
- and ^ 
- or v
- implication -> 
- biconditional <->
those are the five most used logical conneters .

we motly use logical connectives using a true table. 

*not*
| p | ~p |
|---|---|
|true|false|
|false|true|

*and*

| p | q | p ^ q|
|---|---|---|
|false|false|false|
|false|true|false|
|true|false|false|
|true|true|true|

*or*
| p | q | p or q |
|---|---|---|
|false|false|false|
|false|true|true|
|true|false|true|
|true|true|true|


*note* there is exlusive or where when both are true then it is false.

*implication* (->)

| p | q | p->q |
|---|---|---|
|false|false| true|
|false|true|true|
|true|false|false|
|true|true|true|

*biconditional*(<->)(you can read it as if and only if )

| p | q | p<->q |
|---|---|---|
|false|false| true|
|false|true|false|
|true|false|false|
|true|true|true|

**model**: assignment of a truth value to every propositional sysmbol(a `possible world`)

for example 
p: it is raining,
q: it is tuesday.


(p=true,q=false)
what does this is a model.


if there are n sentensene there can be 2^n models. 

**knowledge base**:

a set of sentences known by a knowledge-based agent. 

**Entailment**: look at the symbol online: |= 

for example alpha entails beta

in every model in which sentence alpha is true, sentence beta is also true. 


**inference**
the process of deriving new sentences from old ones. 

there are different algorithm used in this can one of them is:
*model checking*

to determine if KB|= alpha:
    - enumerate all possible models. 
    - if in every model where KB is true , apha is true, then KB entains alpha. 
    - otherwise ,KB does not entail apha. 

this process is called knowledge engineering 

**modus pones**

modus ponens , also known as the law of detachment or affirming the antecedent, is a fundamental rule of inference in logic . its a valid argument form that allows us to deduce a conclusion based on two premises

    If P, then Q. (This is the conditional statement.)
    P. (This affirms the antecedent of the conditional statement.)

Conclusion:

Therefore, Q.

In simpler terms:

If we know that "if P is true, then Q is true," and we also know that "P is true," then we can logically conclude that "Q is true."

Example:
    Premise 1: If it rains, then the ground gets wet.
    Premise 2: It is raining.
    Conclusion: Therefore, the ground gets wet.


Modus Ponens:
    Focus: A fundamental rule of inference in logic. It's a basic step in deductive reasoning, allowing us to draw conclusions based on a conditional statement and the affirmation of its antecedent.
    Application: Primarily used in knowledge representation and reasoning systems, such as expert systems and theorem provers. It helps to derive new knowledge from existing facts and rules.   

    Scope: Limited to applying a specific rule of inference to derive conclusions within a logical framework.

Model Checking:
    Focus: A formal verification technique used to systematically check whether a given system (model) satisfies a specific property (specification).   

Application: Widely used in hardware and software verification to ensure correctness and find potential errors. It can also be applied to analyze complex systems like communication protocols and biological systems.  
Scope: More comprehensive than modus ponens, as it involves exploring the entire state space of a system to check for property violations.



*and elimination*

a and b can concude a 
a and b can conclude b 

*double negation elimination*
it is not true that harry did not pass the test can conclude harry passed the test.
*implicaion elimination*

if it is raining , then harry is inside can conclude it is not raining or harry is inside. 
*biconditional elimination*

a <->b concude:

(a->b) or (b->a)

*de morgans law*

it is not true that both harry and ron passed the test. conclude:
harry did not pass the test or ron did not pass the test. 
~(a and b) conclude: ~a or ~b this is demorgan law


or it can be 
~(a  or b) conclude: ~a and ~b

you can also look at *distributive property*


**Theorem Proving**
- inital state: starting knowledge base
- actions: inference rules
- transistion model: new knowledge base after inference.
- goal test: check statement were tyring to prove
- path cost function: number of steps in prooof


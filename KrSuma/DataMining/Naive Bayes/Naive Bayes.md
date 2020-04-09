### Naive Bayes methods

- With nearest neighbor methods, it is difficult to quantify confidence about a classification.
- With probabilistic methods, we can not only make a classification but we can make probabilistic classifications.
e.g) this athlete is 80% likely to be a basketball player, this customer is 70% likely to make a purchase within the next 5 days, etc.

Nearest neighbour approaches are 'lazy learners' because they just basically remember the set.

Bayesian methods are 'eager learners', in the sense that they analyze the data and build a model immediately given the training set.
They tend to classify instances faster than the latter.

Two main advantages of Bayesian methods:
1. The ability to make probabilistic classifications
2. 'eager learners'

####Probability

P(heads) = 0.5  
the probability for the coin to be heads

P(h|D) 
the probability of the hypothesis h given some data D.

The formula is:

<a href="https://www.codecogs.com/eqnedit.php?latex=P(A|B)&space;=&space;\frac{P(A&space;\cap&space;B)}{P(B)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(A|B)&space;=&space;\frac{P(A&space;\cap&space;B)}{P(B)}" title="P(A|B) = \frac{P(A \cap B)}{P(B)}" /></a>

where P(h) is called the prior probability of h, and P(h|D) is called the psoterior probability of h (probability of h after observing d).

The Naives Bayes Theorem describes the relationship:

<a href="https://www.codecogs.com/eqnedit.php?latex=P(A|B)&space;=&space;\frac{P(B|A)P(A)}{P(B)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(A|B)&space;=&space;\frac{P(B|A)P(A)}{P(B)}" title="P(A|B) = \frac{P(B|A)P(A)}{P(B)}" /></a>

In a classification task, we have a number of possible hypotheses: h1, h2, ... hn. Once we compute all these probabilities, we will pick the hypothesis with the highest probability, called the Maximum a Posteriori hypothesis.

<a href="https://www.codecogs.com/eqnedit.php?latex=h_{MAP}&space;=&space;arg&space;max_{h\in&space;H}\frac{P(B|A)P(A)}{P(B)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?h_{MAP}&space;=&space;arg&space;max_{h\in&space;H}\frac{P(B|A)P(A)}{P(B)}" title="h_{MAP} = arg max_{h\in H}\frac{P(B|A)P(A)}{P(B)}" /></a>

Suppose we have items A, B, and C. Let D represent the facts we know about the customer.
We want to know which item this customer would be likely to purchase.

We will calculate the P(A|D), P(B|D), and P(C|D) then choose the one with the highest probability.



 
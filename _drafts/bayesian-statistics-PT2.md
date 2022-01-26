---
tags: statistics
---

# Chapter 2+ Bayesian Statistics the Fun Way, by Will Kurt  

## Probability and 'negation'

There must be an explanation for this choice of explanation -

>Another important part of logic is negation. When we say “not true” we
mean false. Likewise, saying “not false” means true. We want probability to
work the same way, so we make sure that the probability of X and the negation of the probability of X sum to 1 (in other words, values are either X, or
not X). We can express this using the following equation:
P(X)+¬P(X) = 1 (Kurt 38)
- ¬ in this equation means the negation

Kurt continues on about the fundamentals of this math P(X)+¬P(X) = 1 when really it seems easier to just say that the probability of something happening and the probability of something not happening must add to 1. Either my favorite actress wins the best actress Oscar or she doesn't. The sample is either predicted class A or class B... but perhaps the concept of negation carries over past this textbook.

## Odds and probability

This is something that I have struggled with remembering/comprehending for a while now, and Kurt introduces it well here, I'll continue forward with my own example.

Calculating the probability of your _belief_ in something can be calculated if you're willing to make a bet on it...

Lets say you are very confident in your ability to absolutely brick your best friend in a game of Super Smash Bros., so confident in fact, you put down a fair wager... "If I win, you only owe me $10, but if you win I'll happily send you a personalized venmo for $500"

With this bet, you have already assigned a probability your belief in your ability to beat your friend in a game of Smash. Lets work through it.

500 to 10, this is the bet you made to your friend, and is actually the equation for odds. _m_ to _n_ or _m_/_n_.

>Your odds represent how many times more strongly you believe there _isn’t_ an article than you believe there _is_ an article. (Kurt 38)

In our case, you believe:  
P(H<sub>I will win the Smash match</sub>) = 500, P(H<sub>My friend will win the Smash match</sub>) = 10 = 500/10 = 50

You believe you are _fifty_ time more likely to win than lose. And now we can assign a probability to this...

If you believe the P(H<sub>I will win the Smash match</sub>) is 50x more likely than P(H<sub>My friend will win the Smash match</sub>) (lets switch to A and B to save space), then you believe P(H<sub>a</sub>) = 50 * P(H<sub>b</sub>). And since we _know_ from above that the probability of something happening and the probability of something not happening must add to 1, in this case that P(H<sub>a</sub>)+¬P(H<sub>a</sub>) = 1. And here the ¬P(H<sub>a</sub>) is just P(H<sub>b</sub>), _now_ we can get to the good stuff, algebra.


***

[Bayesian Statistics, The Fun Way, by Will Kurt](https://nostarch.com/learnbayes)

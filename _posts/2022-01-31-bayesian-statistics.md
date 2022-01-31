---
tags: statistics
---

# Starting Bayesian Statistics the Fun Way, by Will Kurt

So far this is an awesome book and I am looking forward to the rest, be sure to check it out.

In order to help myself understand some of the initial topics brought forward in literally the opening chapters of the book, I had to go out and research the formal definition of frequentist statistics.

## What is Frequentist Stats?
The frequentist approach to stats is all about frequencies, distributions, and the law of large numbers. Taking the coin flip, if a fair coin is flipped an infinite number of times, one can expect to get an equal number of heads and tails. Or a probability of getting a heads (or tails) being .5 per flip based on this observed frequency. And therefore the fair coin flip has a binomial distribution of outcomes over infinite coin flips. The reason all of the infinities are important (law of large numbers) is that frequentist statistics only applies probabilities to repeated events observed over long periods of time.<sup>1</sup> And it's in this area that frequentism is apparently very different from Bayesian stats.

## What is Bayesian Statistics?
So far, this is something I can comprehend on my own. However, since I have had a hard time figuring out how to explain the difference between Bayesian stats and frequentist stats without immediately quoting Will Kurt or another more experienced statistician. I can't say I fully comprehend it. You don't fully understand something until you can teach it right?

I'll leave it up to Kurt here -

>Bayesian statistics, on the other hand, is concerned with how probabilities represent how uncertain we are about a piece of information. In Bayesian
terms, if the probability of getting heads in a coin toss is 0.5, that means we
are equally unsure about whether we’ll get heads or tails. For problems like
coin tosses, both frequentist and Bayesian approaches seem reasonable, but
when you’re quantifying your belief that your favorite candidate will win the
next election, the Bayesian interpretation makes much more sense. (Kurt 21)

Kurt does a pretty good job at introducing Bayesian statistics, and how the general thought process of Bayesian stats in pretty in tune with normal logical reasoning.
I really like the example of an election, there are no real previous elections to help predict the outcome here (unless this is a second term something) but for examples sake, we'd be predicting the outcome of an election based on all the prior data collected during campaigns. Things like policies, primaries, T.V. appearances, pop culture knowledge, etc. would all influence the conditional probability of an election type event. This example, for me, clearly separates what is a Bayesian thought process from a frequentist problem. In election type events there may not always be a frequency distribution or repeated events to pull a probability from.

This comparison ends it here and covers the one crucial detail of the first chapter without going into some of the basic math exercises Kurt does to put probabilities into equations.


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

Calculating the probability of your _belief_ in something can be calculated if you're willing to make a bet on it...

Lets say you are very confident in your ability to absolutely brick your best friend in a game of Super Smash Bros., so confident in fact, you put down a fair wager... "If I win, you only owe me $10, but if you win I'll happily send you a personalized venmo for $500"

With this bet, you have already assigned a probability your belief in your ability to beat your friend in a game of Smash. Lets work through it.

500 to 10, this is the bet you made to your friend, and is actually the equation for odds. _m_ to _n_ or _m_/_n_.

>Your odds represent how many times more strongly you believe there _isn’t_ an article than you believe there _is_ an article. (Kurt 38)

In our case, you believe:  
P(H<sub>I will win the Smash match</sub>) = 500, P(H<sub>My friend will win the Smash match</sub>) = 10 = 500/10 = 50

You believe you are _fifty_ time more likely to win than lose. And now we can assign a probability to this...

If you believe the P(H<sub>I will win the Smash match</sub>) is 50x more likely than P(H<sub>My friend will win the Smash match</sub>) (lets switch to A and B to save space), then you believe P(H<sub>a</sub>) = 50 * P(H<sub>b</sub>). And since we _know_ from above that the probability of something happening and the probability of something not happening must add to 1, P(H<sub>a</sub>)+¬P(H<sub>a</sub>) = 1. And here the ¬P(H<sub>a</sub>) is just P(H<sub>b</sub>), _now_ we can get to the good stuff, algebra.

So, P(H<sub>a</sub>) = 50 * P(H<sub>b</sub>), and P(H<sub>a</sub>)+¬P(H<sub>a</sub>) = 1, therefore...  
P(H<sub>a</sub>) = 50 * (1 - P(H<sub>a</sub>)) =  
P(H<sub>a</sub>) = 50 - 50 * P(H<sub>a</sub>))... now add 50 * P(H<sub>a</sub>)) to both sides...  
51 * P(H<sub>a</sub>) = 50... and divide both sides by 51  
P(H<sub>a</sub>) = 50/51  
50/51 = .98 = P(H<sub>a</sub>)  

Now all this math quantifies your _belief_ that you will 3 stock your best friend on final destination. You might be overconfident.  

Now what did all this teach us?  

That we can generalize the equation for converting odds to probability to...

P(H) = O(H) / 1+O(H)  

Where O = Odds. You can try it for yourself. The 1 comes from adding P(H) to both sides where we end up adding P(H) to P(H).

This summarizes Kurt's introduction to odds to odds and is very well done.

## Probability _and_ the product rule

I won't spend long here because it seems simple enough. The probability of A _and_ B occurring is simply P(A) * P(B). The product of A and B.  

Here is a simple graph representation of why P(A,B) = P(A) * P(B), and also my submission to the Louvre.  

Probability of flipping two tails when flipping two quarters:  
![some quarters](/images/quarter-art.png)
Here we can clearly see that there is only one path out of four that results in two tails.  
1/4 = .25  
We also know that the P(Flipping Tails) = .5 in a perfect world. So if flipping tails is event A
and flipping tails is also event B we get...  

P(A, B) = P(Flipping Tails, Flipping Tails) =  
P(Flipping Tails, Flipping Tails) =  P(Flipping Tails) * P(Flipping Tails) =  
P(Flipping Tails, Flipping Tails) = .5 * .5 = .25 = 1/4. Perfect.

***

[Bayesian Statistics, The Fun Way, by Will Kurt](https://nostarch.com/learnbayes)  
<sup>1</sup>: [http://jakevdp.github.io/blog/2014/03/11/frequentism-and-bayesianism-a-practical-intro/](http://jakevdp.github.io/blog/2014/03/11/frequentism-and-bayesianism-a-practical-intro/)

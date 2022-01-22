---
tag: statistics
---

# Intro
For the purpose of my own learning and general aversion to boredom, I will go cover to cover of _Bayesian Statistics The Fun Way_, by Will Kurt. I'm going to keep a record of things I struggle with while going cover to cover while also generating use cases as to why knowing bayesian stats is useful for someone working in a Data Science capacity. There may be no necessity to know bayesian statistics or more than its fundamentals... But either way I'll learn something.

## Update 1/22/2022
~~There may be no necessity to know bayesian statistics~~ This was a dumb statement. There is definitely a necessity to understand probabilistic modeling of things. For example, probabilistic approaches to hyperparameter tuning of machine learning models. GridSearchCV and RandomSearchCV are both standard ways to tune models. But when searching gigantic parameter spaces they are _slow_. GridSearchCV will attempt every combination of your parameter grid and save the better iteration every time. This means no stone goes unturned at the cost of time. RandomSearch will just randomly try combinations a specified number of times and return the best parameters as well, here you are at the mercy of chance that there wasn't a better parameter set it didn't try. And if that explanation was terrible, here is a two sentence summary of their similarity: GridSearch and RandomSearch are both _uninformed_ forms of optimization, they try and forget on repeat and store the results for you to look at later. They do not choose their next set of parameters with an educated guess of what might be a better set of parameters based on their past evaluations.

Now Bayesian Optimization is pretty neat... (this update is made before reading much of the textbook and is just a thought dump of on the job learning).

# an excuse to practice my MD.md

## A list of important topics I feel are a necessity to understand conversationally without the use of visual aides lol. I will post a succint explanation underneath each point I feel explains the topic well enough and is created off the cuff.

# List of topics to review
## Here lies a list of topics I need to review/would not feel comfortable teaching unprepared
- Odds, Probability and _logOdds_
  - Odds is the _ratio_ of something occuring vs not. I.E 4/6, 4 wins and 6 losses but _10 instances_. Probability on the other hand is the ration of something happenening against _all possible happenings_, the odds scenario expressed as a probability in the same situation would be 4/10, 4 wins over _10 instances_. Odds can exceed 1, in the previous example the odds of a negative instance are 6/4 or 1.5.

  - LogOdds, is the log(odds). It is used because regular odds are on a scale from 0 - positive infinity. Intuitively this makes sense, odds ratios deal with real instances (games, diagnoses, conditions), so there can't be less than 0 instances in a given scenario. -1 wins to 4 losses out of 5 games makes no sense. But 1 win vs. possibly infinite losses is totally plausible. An example from popular sports... out of 72 played seasons, the Cleveland Browns have had **_0_** superbowl appearances. So their odds of appearing can be expressed as 0/72, or 0. While their odds of not making an apperance can be expressed as 72/0 which is actually expressed as positive infinity when talking about odds. I need a better example here.

- Logistic regression and its predictions in logOdds

- Naive Bayes and its importance

- [x] Supprt vector machines and their line-fitting
  - SVM's are linear discriminant functions, they fit a line to the data that maximizes the distance between the two classes in the data. The thicc-bar's center is the discriminant and the leftover space is the margin. _The function that maximizes this margin boudary gives the maximal leeway for classifying points_. Therefore, in order for a new instance to be misclassified it would need to be obscenely close to the line or on the other side. And if that is the case your model should be re-evaluated or the instance inspected.

- Linear regression honestly, fitting a line, minimizing least squared errors from that line

- Class probability estimation and Logistic regressions

- Feature Engineering
  - Polynomial feature engineering is a thing, multiplying numeric or expressed-as-numeric features together in order to express an interaction if there even is one
  - What's better is taking columns with high _cardinality_ and reducing that down through frequency counts. Here's that from python.
    - fbc = pd.Series.value_counts(df['FabricColor']) fbc.name = 'FabricColorCount'
  - Here we have created a series of the unique values seen in the column 'FabricColor', its index is each of the unique values and it has one column containing the unique values we want. It is also named the column we had transformed, and we gotta rename it for the next step.
    - df.join(fbc, on='FabricColor')
  - We join it back onto our dataframe we created it from using .join _this is why we renamed it_. If it had retained its original name 'FabricColor' it would have thrown an error when we tried to reference the dataframes['FabricColor'] in the .join method.
- 

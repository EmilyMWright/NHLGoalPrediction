# NHL Goal Prediction

## Predicting goals in event sequences using Kaggle NHL Game Data.

### Introduction
 The problem of predicting rare events in event sequences has numerous applications such as anticipating equipment failures or cyber attacks. The purpose of this analysis is to use a machine learning algorithm to monitor sequences of events and predict when goals will occur during National Hockey League (NHL) games.

 The [NHL Game Data](https://www.kaggle.com/martinellis/nhl-game-data?select=game_plays.csv) from Kaggle contains information about events that occur during NHL games such as type, time, team, and location. It spans 11244 games from the 2011-12 season to the 2017-18 season. 9000 games (about 80%) will be used to train the algorithm and the remainder to evaluate it. 
 
 ### Method
 The pandas DataFrame sample method was used to return 9000 unique game ids. The games corresponding to these ids were saved to the train_plays.csv while the remainder were saved to eval_plays.csv.

 A monitoring time and warning time were selected. The monitoring time indicates the window of events that the algorithm considers at any one instant. Typically, a longer monitoring time leads to better predictions, however too large of a monitoring time would lead to meaningless predictions. The warning time is the minimum length of time prior to a goal at which a prediction is useful.

 The monitoring time was calculated from the average time between faceoffs. Thus, it will be that once a potential "goal-leading" sequence has been identified, the next faceoff will probably be the last before the goal is likely to occur. The monitoring time was found to be 64.5 seconds, which rounds easily to one minute.

 The warning time was determined using the average time between a goal and the last faceoff prior to the goal. This pause in play will allow coaches to change up players or even take a time out if it seems that a goal is iminent. The warning time was found to be 61.3 seconds, which was also rounded to one minute.

 There are two conditions which make a sequence of events a good candidate for predicting goals.
 1. Frequency: the sequence occurs in the lead-up to many goals
 2. Accuracy: the sequence does not often occur if no goal is forthcoming

 The training algorithm identified all three play sequences which occurred between 2 minutes and 1 minute prior to a goal in the training data. It is important to note that each play in a sequence consisted of both an event (Faceoff, Giveaway, Blocked Shot, Shot, Hit, Goal, Penalty, Takeaway, Missed Shot) and a team (goal scoring or defending). The algorithm then searched for the identified sequences in all three play sequences which were not in the lead-up to a goal in order to find false positives. In this case, there was no goal scoring team, so each sequence of events corresponded to two sequences of plays (one for each team in the game to be considered the potential goal scorer). 

 ### Results
 ...TODO

 
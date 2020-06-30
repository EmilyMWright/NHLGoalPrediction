# NHL Goal Prediction

## Predicting goals in event sequences using Kaggle NHL Game Data.

 The problem of predicting rare events in event sequences has numerous applications such as anticipating equipment failures or cyber attacks. The purpose of this analysis is to use a machine learning algorithm to monitor sequences of events and predict when goals will occur during National Hockey League (NHL) games.

 The NHL Game Data from Kaggle contains information about events that occur during NHL games such as type, time, team, and location. It spans 11,244 games from the 2011-12 season to the 2017-18 season. 9,000 games (about 80%) will be used to train the algorithm and the remainder to evaluate it. 

 To begin, a monitoring time and warning time must be selected. The monitoring time indicates the length of the sub-sequence of events that the algorithm considers at any one instant. Typically, a longer monitoring time leads to better predictions, however too large of a monitoring time would lead to meaningless predictions. The warning time is the minimum length of time prior to a goal at which a prediction is useful.

 The warning time was determined using the average time between a goal and the last faceoff prior to the goal. This pause in play will allow coaches to change up players or even take a time out if it seems that a goal is iminent. The WarningTime script found the mean time to be 55 seconds.

 The monitoring time was be calculated from the average time between faceoffs. Thus, it will be that once a potential "goal-leading" sequence has been identified, the next faceoff to occur will probably be the last before the goal is likely to occur. The MonitoringTime script found the average time to be 60 seconds.

 Next the data was split into training and evaluation sets. The pandas DataFrame sample method was used to return 9000 unique game ids. The games corresponding to these ids were saved the train_plays.csv while the remainder were saved to eval_plays.csv.

 For each goal in the training set, the event sequence in the monitoring time (60 seconds) which ended at the warning time (55 seconds) prior to said goal was recorded in a csv.
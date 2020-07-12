import pandas as pd
import csv

# Loads and cleans data
event_headers = ['event', 'play_id', 'periodTime', 'team_id_for']
event_df = pd.read_csv('train_plays.csv', usecols = event_headers)

events = ['Faceoff', 'Giveaway', 'Blocked Shot', 'Shot', 'Hit', 'Goal', 'Penalty', 'Takeaway', 'Missed Shot']

event_df = event_df[event_df.event.isin(events)].reset_index()
goal_df = event_df[event_df.event == 'Goal'].reset_index()

goals = pd.read_csv('top_three_play_sequences.csv').IncludedIn

warned_goals = []
for goal in goals:
    warned_goals += eval(goal)

warned_goals = list(set(warned_goals))

warned_goals_df = event_df[event_df.play_id.isin(warned_goals)]

indices = warned_goals_df.index
times = warned_goals_df.periodTime.to_list()

to_drop = []
for j in len(warned_goals):
    i = indices[j] - 1
    t = times[j]
    if t > 115:
        min_t = t - 115
    else:
        min_t = 0

    prev_t = 1200
    
    while ((t > min_t) & (t < prev_t) & (i > 0)):
        to_drop += i
        i = i - 1
        prev_t = t
        t = event_df.iloc[i].periodTime

event_df.drop(to_drop, inplace = True)

period_dfs = event_df.groupby(['game_id', 'period'])



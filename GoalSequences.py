import pandas as pd
import csv

# Loads and cleans data
event_headers = ['event', 'periodTime', 'team_id_for']
event_df = pd.read_csv('game_plays.csv', usecols = event_headers)

events = ['Faceoff', 'Giveaway', 'Blocked Shot', 'Shot', 'Hit', 'Goal', 'Penalty', 'Takeaway', 'Missed Shot']

event_df = event_df[event_df.event.isin(events)].reset_index()
goal_df = event_df[event_df.event == 'Goal'].reset_index()
indices = goal_df.level_0
times = goal_df.periodTime
teams = goal_df.team_id_for

with open('goal_sequences.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    for j in range(len(goal_df)):
        i = indices[j]
        t = times[j]
        team = teams[j]
        sequence = []
        if t > 55:
            min_t = t - 55
        else:
            min_t = 0
        while (event_df.iloc[i].periodTime > min_t):
            if event_df.iloc[i].team_id_for == team:
                sequence.append('O' + event_df.iloc[i].event)
            else:
                sequence.append('D' + event_df.iloc[i].event)
            i = i - 1
        writer.writerow(sequence)
    


import pandas as pd
import csv

# Loads and cleans data
event_headers = ['event', 'play_id', 'periodTime', 'team_id_for']
event_df = pd.read_csv('train_plays.csv', usecols = event_headers)

events = ['Faceoff', 'Giveaway', 'Blocked Shot', 'Shot', 'Hit', 'Goal', 'Penalty', 'Takeaway', 'Missed Shot']

event_df = event_df[event_df.event.isin(events)].reset_index()
goal_df = event_df[event_df.event == 'Goal'].reset_index()

# saves goal lead-up sequences to csv
indices = goal_df.level_0
times = goal_df.periodTime
teams = goal_df.team_id_for
p_ids = goal_df.play_id

with open('between_sequences.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    for j in range(len(goal_df)):
        i = indices[j]
        if j > 0:
            k = indices[j-1]
        else:
            k = 0
        
        t = times[j]
        team = teams[j]
        p_id = p_ids[j]
        sequence = []
        if t > 115:
            sequence.append(p_id)
            min_t = t - 115
            while (event_df.iloc[i].periodTime > min_t):
                i = i - 1
            while ((event_df.iloc[i].periodTime > 0) & (i > k)):
                if event_df.iloc[i].team_id_for == team:
                    sequence.append('O' + event_df.iloc[i].event)
                else:
                    sequence.append('D' + event_df.iloc[i].event)
                i = i - 1
            writer.writerow(sequence)
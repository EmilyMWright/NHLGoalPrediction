import pandas as pd
import csv

headers = ['play_id']
for i in range(25):
    headers.append("Play" + str(i + 1))

leadup_df = pd.read_csv('goal_sequences.csv', names = headers)
leadup_df = leadup_df[leadup_df.count(axis='columns') >= 4]

with open('three_play_sequences.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    for index, seq in leadup_df.iterrows():
        for i in range(seq.count() - 3):
            three_plays = [seq.play_id]
            three_plays.append(seq["Play" + str(i + 1)])
            three_plays.append(seq["Play" + str(i + 2)])
            three_plays.append(seq["Play" + str(i + 3)])
            writer.writerow(three_plays)
    
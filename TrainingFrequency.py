import pandas as pd
import numpy as np

sequences_df = pd.read_csv('three_play_sequences.csv', names = ['play_id','play1', 'play2', 'play3'])
sequences_df = sequences_df.drop(['play_id'], axis=1).drop_duplicates()

headers = ["play_id"]
for i in range(24):
    headers.append("Play" + str(i + 1))

leadup_df = pd.read_csv('goal_sequences.csv', names = headers).fillna("")
leadup_df['OneString'] = leadup_df.loc[:,headers[1:]].sum(axis = 1)
sequences_df['OneString'] = sequences_df.loc[:,['play1', 'play2', 'play3']].sum(axis = 1)

freqs = []
p_id_lists = []
for sub_str in sequences_df['OneString']:
    freq = 0
    p_ids = []
    for index, row in leadup_df.iterrows():
        sup_str = row['OneString']
        p_id = row['play_id']
        if sub_str in sup_str:
            freq = freq + 1
            p_ids.append(p_id)
    freqs.append(freq)
    p_id_lists.append(p_ids)

sequences_df['Frequency'] = freqs
sequences_df['IncludedIn'] = p_id_lists
print(sequences_df.sort_values(['Frequency'], ascending=False).head())
sequences_df.Frequency.nlargest(200).to_csv('top_three_play_sequences.csv')

    
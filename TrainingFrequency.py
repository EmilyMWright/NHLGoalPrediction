import pandas as pd

sequences_df = pd.read_csv('three_play_sequences.csv', names = ['play1', 'play2', 'play3'])
sequences_df['Level'] = sequences_df.index

sequences_df['Freq'] = sequences_df.groupby(['play1', 'play2', 'play3'])['Level'].transform('count')

sequences_df = sequences_df.drop('Level', axis=1).drop_duplicates()

print(len(sequences_df))
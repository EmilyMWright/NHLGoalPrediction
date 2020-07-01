import pandas as pd

sequences_df = pd.read_csv('three_play_sequences.csv', names = ['play1', 'play2', 'play3'])
sequences_df['Level'] = sequences_df.index

sequences_df['Count'] = sequences_df.groupby(['play1', 'play2', 'play3'])['Level'].transform('count')

sequences_df = sequences_df.drop('Level', axis=1).drop_duplicates()

floor = sequences_df.Count.nlargest(200).min()
top_sequences_df = sequences_df[sequences_df.Count >= floor].sort_values(['Count'], ascending = False)

top_sequences_df.to_csv('top_three_play_sequences.csv')
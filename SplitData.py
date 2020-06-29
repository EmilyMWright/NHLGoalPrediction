import pandas as pd

event_df = pd.read_csv('game_plays.csv')

train_ids = event_df.game_id.sample(n=9000)

train_df = event_df[event_df.game_id.isin(train_ids)].reset_index()
eval_df = event_df[~event_df.game_id.isin(train_ids)].reset_index()

train_df.to_csv('train_plays.csv')
eval_df.to_csv('eval_plays.csv')
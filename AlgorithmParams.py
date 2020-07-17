import pandas as pd

def last_faceoff(event_df):
    faceoff_df = event_df[event_df.event == 'Faceoff']
    faceoff_df = faceoff_df.dropna(subset = ['next_goal_id'])
    time_from_faceoff = faceoff_df.groupby(['next_goal_id'])['time_to_goal'].min().mean()
    print("The average time between a goal and the faceoff that precedes it is", time_from_faceoff, "seconds.")

def load_events(event_file):
    event_df = pd.read_csv(event_file)
    last_faceoff(event_df)

load_events('updated_train_plays.csv')
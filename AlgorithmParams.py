import pandas as pd

def preceding_faceoff(event_df):
    faceoff_df = event_df[event_df.event == 'Faceoff']
    faceoff_df = faceoff_df.dropna(subset = ['next_goal_id'])
    time_from_faceoff = faceoff_df.groupby(['next_goal_id'])['time_to_goal'].min().mean()
    print("The average time between a goal and the faceoff that precedes it is", time_from_faceoff, "seconds.")

def between_faceoffs(event_df):
    faceoff_df = event_df[event_df.event == 'Faceoff']
    time_between_faceoffs = 1200/faceoff_df.groupby(['game_id', 'period'])['event'].count().mean()
    print("The average time between faceoffs is", time_between_faceoffs, "seconds.")


def load_events(event_file):
    event_df = pd.read_csv(event_file)
    #preceding_faceoff(event_df)
    between_faceoffs(event_df)

load_events('updated_train_plays.csv')
import pandas as pd

def warning_time(event_df):
    ''' Print average time between a goal and the faceoff that precedes it '''
    faceoff_df = event_df[event_df.event == 'Faceoff']
    faceoff_df = faceoff_df.dropna(subset = ['next_goal_id'])
    time_from_faceoff = faceoff_df.groupby(['next_goal_id'])['time_to_goal'].min().mean()
    print("The average time between a goal and the faceoff that precedes it is", time_from_faceoff, "seconds.")

def monitoring_time(event_df):
    ''' Print average time between faceoffs that precedes it '''
    faceoff_df = event_df[event_df.event == 'Faceoff']
    time_between_faceoffs = 1200/faceoff_df.groupby(['game_id', 'period'])['event'].count().mean()
    print("The average time between faceoffs is", time_between_faceoffs, "seconds.")

def main():
    event_df = pd.read_csv('updated_train_plays.csv')
    warning_time(event_df)
    monitoring_time(event_df)

if __name__ == '__main__':
    main()
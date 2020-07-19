import pandas as pd
import numpy as np

def next_goal(period_df):
    ''' Add columns with data about upcoming goal and return updated dataframe '''
    period_df.reset_index(inplace = True)
    goal_df = period_df[period_df.event == 'Goal']
    next_goals = []
    goal_times = []
    goal_attrs = []

    j = -1
    for i in goal_df.index:
        goal = goal_df.loc[i]
        next_goals += [goal.play_id]*(i-j)
        goal_times += [goal.periodTime]*(i-j)
        goal_attrs += [goal.attr_event]*(i-j)
        j = i

    nan_end = [np.nan]*(len(period_df) - len(next_goals))
    period_df['next_goal_id'] = next_goals + nan_end
    period_df['next_goal_time'] = goal_times + nan_end
    period_df['next_goal_attr'] = goal_attrs + nan_end
    period_df['time_to_goal'] = period_df.next_goal_time - period_df.periodTime
    return period_df
    
def get_sequences(period_df):
    ''' Add columns with sequences of data about previous three plays and return updated dataframe '''
    events = period_df.event.to_list()
    period_df['event_seq'] = [np.nan, np.nan] + [[x,y,z] for x,y,z in zip(events[:-2], events[1:-1], events[2:])]
    attr_events = period_df.attr_event.to_list()
    period_df['attr_event_seq'] = [np.nan, np.nan] + [[x,y,z] for x,y,z in zip(attr_events[:-2], attr_events[1:-1], attr_events[2:])]
    return period_df

def add_period_cols(period_df):
    ''' Call functions to add columns to dataframe representing one NHL period and return updated dataframe '''
    return get_sequences(next_goal(period_df))

def attribute_events(game_df):
    ''' Add columns attributing each event to team A (wins first faceoff) or B and return updated dataframe '''
    a_team = game_df.iloc[0].team_id_for
    game_df['attr_event'] = np.where(game_df.team_id_for == a_team, True, False)

def add_game_cols(game_df):
    ''' Call functions to add columns to dataframe representing one NHL game and return updated dataframe '''
    attribute_events(game_df)
    game_df = game_df.groupby(['period'], sort = False).apply(add_period_cols)
    return game_df

def add_event_cols(event_file):
    ''' Load event data, add columns, write updated dataframe to csv '''
    event_headers = ['event', 'game_id', 'play_id', 'periodTime', 'period','team_id_for']
    event_df = pd.read_csv(event_file, usecols = event_headers)
    event_names = ['Faceoff', 'Giveaway', 'Blocked Shot', 'Shot', 'Hit', 'Goal', 'Penalty', 'Takeaway', 'Missed Shot']
    event_df = event_df[event_df.event.isin(event_names)].reset_index()
    updated_event_file = 'updated_' + event_file
    event_df.groupby(['game_id'], sort = False).apply(add_game_cols).to_csv(updated_event_file)

def main():
    add_event_cols('train_plays.csv')

if __name__ == "__main__":
        main()
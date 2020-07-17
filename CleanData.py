import pandas as pd
import numpy as np
import csv

def NextGoal(period_df):
    period_df.reset_index(inplace = True)
    goal_df = period_df[period_df.event == 'Goal']
    next_goals = []
    goal_times = []
    goal_attrs = []
    j = 0
    for i in goal_df.index:
        goal_id = goal_df.loc[i].play_id
        goal_time = goal_df.loc[i].periodTime
        goal_attr = goal_df.loc[i].attr_event
        next_goals += [goal_id]*(i-j+1)
        goal_times += [goal_time]*(i-j+1)
        goal_attrs += [goal_attr]*(i-j+1)
        j = i + 1
    nan_end = [np.nan]*(len(period_df) - len(next_goals))
    next_goals += nan_end
    goal_times += nan_end
    goal_attrs += nan_end

    period_df['next_goal_id'] = next_goals
    period_df['next_goal_time'] = goal_times
    period_df['next_goal_attr'] = goal_attrs
    period_df['time_to_goal'] = period_df.next_goal_time - period_df.periodTime

    return period_df
    
def GetSequences(period_df):
    events = period_df.event.to_list()
    period_df['event_seq'] = [np.nan, np.nan] + [[x,y,z] for x,y,z in zip(events[:-2], events[1:-1], events[2:])]

    attr_events = period_df.attr_event.to_list()
    period_df['attr_event_seq'] = [np.nan, np.nan] + [[x,y,z] for x,y,z in zip(attr_events[:-2], attr_events[1:-1], attr_events[2:])]
    return period_df

def AddPeriodCols(period_df):
    return GetSequences(NextGoal(period_df))

def AttributeEvents(game_df):
    a_team = game_df.iloc[0].team_id_for
    game_df['attr_event'] = np.where(game_df.team_id_for == a_team, 'A', 'B')

def AddGameCols(game_df):
    AttributeEvents(game_df)
    game_df = game_df.groupby(['period'], sort = False).apply(AddPeriodCols)
    return game_df

event_headers = ['event', 'game_id', 'play_id', 'periodTime', 'period','team_id_for']
event_df = pd.read_csv('train_plays.csv', usecols = event_headers)

event_names = ['Faceoff', 'Giveaway', 'Blocked Shot', 'Shot', 'Hit', 'Goal', 'Penalty', 'Takeaway', 'Missed Shot']

event_df = event_df[event_df.event.isin(event_names)].reset_index()

event_df = event_df.head(n = 1000)

event_df.groupby(['game_id'], sort = False).apply(AddGameCols).to_csv('test_add_cols.csv')
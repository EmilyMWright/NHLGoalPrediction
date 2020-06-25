import pandas as pd
import statistics as stats

# Loads and cleans data
event_headers = ['play_id', 'game_id', 'team_id_for', 'team_id_against', 'event', 'st_x', 'st_y', 'period', 'periodTime']
event_df = pd.read_csv('game_plays.csv', usecols = event_headers)

events_to_keep = ['Faceoff', 'Giveaway', 'Blocked Shot', 'Shot', 'Hit', 'Goal', 'Penalty', 'Takeaway', 'Missed Shot']

event_df = event_df[event_df.event.isin(events_to_keep)].reset_index()

team_id_dict = {1:'NJD', 2:'NYI', 3:'NYR', 4:'PHI', 5:'PIT', \
6:'BOS', 7:'BUF', 8:'MTL', 9:'OTT', 10:'TOR', 11:'ATL', \
12:'CAR', 13:'FLA', 14:'TBL', 15:'WSH', 16:'CHI', 17:'DET', \
18:'NSH', 19:'STL', 20:'CGY', 21:'COL', 22:'EDM', 23:'VAN', \
24:'ANA', 25:'DAL', 26:'LAK', 27:'PHX', 28:'SJS', 29:'CBJ', \
30:'MIN', 52:'WPG', 53:'ARI', 54:'VGK'}

event_df.team_id_for.replace(team_id_dict, inplace=True)
event_df.team_id_against.replace(team_id_dict, inplace=True)

# Finds average time between goal and last faceoff prior to goal
goal_df = event_df[event_df.event.isin(['Goal'])].reset_index()
goal_foff_df = event_df[event_df.event.isin(['Goal', 'Faceoff'])].reset_index()
foff_indices = goal_foff_df[goal_foff_df.event == 'Goal'].index - 1

last_foff_df = goal_foff_df.iloc[foff_indices]

warning_time = stats.mean(goal_df.periodTime.values - last_foff_df.periodTime.values)

print(warning_time)

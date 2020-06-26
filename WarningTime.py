import pandas as pd
import statistics as stats

# Loads and cleans data
event_headers = ['event', 'periodTime']
event_df = pd.read_csv('game_plays.csv', usecols = event_headers)

# Finds average time between goal and last faceoff prior to goal
goal_df = event_df[event_df.event.isin(['Goal'])].reset_index()
goal_foff_df = event_df[event_df.event.isin(['Goal', 'Faceoff'])].reset_index()
foff_indices = goal_foff_df[goal_foff_df.event == 'Goal'].index - 1

last_foff_df = goal_foff_df.iloc[foff_indices]

warning_time = stats.mean(goal_df.periodTime.values - last_foff_df.periodTime.values)

print(warning_time)

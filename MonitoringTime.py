import pandas as pd
import statistics as stats

# Loads and cleans data
event_headers = ['event', 'periodType']
event_df = pd.read_csv('game_plays.csv', usecols = event_headers)

num_games = (event_df.event == 'Game Scheduled').sum()
num_foffs = ((event_df.event == 'Faceoff') & (event_df.periodType == 'REGULAR')).sum()

monitoring_time = num_games*60/num_foffs

print(monitoring_time)
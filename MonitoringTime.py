import pandas as pd

# Loads and cleans data
event_headers = ['game_id', 'event', 'periodTime']
event_df = pd.read_csv('game_plays.csv', usecols = event_headers)
import pandas as pd
import statistics as stats

# Loads and cleans data
event_headers = ['game_id', 'event', 'period', 'periodTime']
event_df = pd.read_csv('game_plays.csv', usecols = event_headers)

foff_df = event_df[event_df.event == 'Faceoff'].reset_index()

periods = [pd.DataFrame(y) for x, y in foff_df.groupby(['game_id', 'period'], as_index=False)]

# Finds average time between faceoffs
print(stats.mean(periods[0].periodTime.values[1:] - periods[0].periodTime.values[:-1]))

#means = []
#for period in periods:
    #means.append(stats.mean(period.periodTime.values[1:] - period.periodTime.values[:-1]))

#monitoring_time = stats.mean(means)

#print(monitoring_time)
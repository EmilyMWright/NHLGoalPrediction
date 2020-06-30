import pandas as pd

headers = []
for i in range(12):
    headers.append("Play" + str(i + 1))

leadup_df = pd.read_csv('goal_sequences.csv', names = headers)
print(leadup_df.count(axis='columns').mean())
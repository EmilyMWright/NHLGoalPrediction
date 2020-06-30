import pandas as pd

headers = []
for i in range(12):
    headers.append("Play" + str(i + 1))

leadup_df = pd.read_csv('goal_sequences.csv', names = headers)
count_df = leadup_df.count(axis='columns')
print(100*count_df[count_df >= 3].count()/count_df.count())
import pandas as pd
import ast
import numpy as np

def unique_sequences(event_df):
    monitored_event_df = event_df[(event_df.time_to_goal < 120) & (event_df.time_to_goal > 60)]
    monitored_event_df.attr_event_seq = [~np.logical_xor(team, seq) for team, seq in 
                                        zip(monitored_event_df.next_goal_attr, monitored_event_df.attr_event_seq)]
    monitored_event_df.event_seq = monitored_event_df.event_seq.apply(tuple)
    monitored_event_df.attr_event_seq = monitored_event_df.attr_event_seq.apply(tuple)
    unique_event_df = monitored_event_df.groupby(['event_seq','attr_event_seq']).size().reset_index(name = 'count')
    print(unique_event_df.sort_values(by = 'count', ascending = False).head())
    # TODO

def main():
    event_headers = ['time_to_goal', 'next_goal_id', 'next_goal_attr', 'event_seq', 'attr_event_seq']
    # event_df = pd.read_csv('updated_train_plays.csv', usecols = event_headers, true_values = ['True'], false_values = ['False'])
    event_df = pd.read_csv('updated_train_plays.csv', usecols = event_headers)
    event_df.dropna(subset = ['event_seq','attr_event_seq'], inplace = True)
    event_df.event_seq = [ast.literal_eval(seq) for seq in event_df.event_seq]
    event_df.attr_event_seq = [ast.literal_eval(seq) for seq in event_df.attr_event_seq]
    
    event_df.next_goal_attr = event_df.next_goal_attr.map({'True' : True, 'False' : False})
    
    unique_sequences(event_df.dropna(subset = ['next_goal_attr']))

if __name__ == '__main__':
    main()
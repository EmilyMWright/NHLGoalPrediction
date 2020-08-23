import pandas as pd
import ast
import numpy as np

def train_frequency(event_df):
    mon_df = event_df[(event_df.time_to_goal < 120) & (event_df.time_to_goal > 60)]
    mon_df['attr_event_seq'] = [~np.logical_xor(team, seq) for team, seq in 
                                        zip(mon_df.next_goal_attr, mon_df.attr_event_seq)]
    mon_df['event_seq'] = mon_df.event_seq.apply(tuple)
    mon_df['attr_event_seq'] = mon_df.attr_event_seq.apply(tuple)
    unique_df = mon_df.groupby(['event_seq','attr_event_seq'])

    mon_count_df = unique_df.size().reset_index(name = 'occurances').sort_values(by = 'occurances', ascending = False)
    
    return mon_count_df

def train_accuracy(event_df):
    flip_df = pd.DataFrame()
    flip_df['event_seq'] = event_df.event_seq
    flip_df['attr_event_seq'] = [np.logical_not(seq) for seq in event_df.attr_event_seq]
    event_df = pd.concat([event_df, flip_df])
    event_df['event_seq'] = event_df.event_seq.apply(tuple)
    event_df['attr_event_seq'] = event_df.attr_event_seq.apply(tuple)
    unique_df = event_df.groupby(['event_seq','attr_event_seq'])

    all_count_df = unique_df.size().reset_index(name = 'total_occurances').sort_values(by = 'total_occurances', ascending = False)
    
    return all_count_df

def main():
    event_headers = ['time_to_goal', 'next_goal_id', 'next_goal_attr', 'event_seq', 'attr_event_seq']
    event_df = pd.read_csv('updated_train_plays.csv', usecols = event_headers)
    event_df.dropna(subset = ['event_seq','attr_event_seq'], inplace = True)
    event_df['event_seq'] = [ast.literal_eval(seq) for seq in event_df.event_seq]
    event_df['attr_event_seq'] = [ast.literal_eval(seq) for seq in event_df.attr_event_seq]
    
    event_df['next_goal_attr'] = event_df.next_goal_attr.map({'True' : True, 'False' : False, True : True, False : False})

    mon_seq_count_df = train_frequency(event_df.dropna(subset = ['next_goal_attr']))
    all_seq_count_df = train_accuracy(event_df)

    eval_df = pd.merge(mon_seq_count_df, all_seq_count_df, how='outer')
    eval_df['percent'] = 100*eval_df.occurances/eval_df.total_occurances
    eval_df.sort_values(by = ['percent', 'occurances', 'total_occurances'], ascending = False, inplace = True)

    eval_df.to_csv('eval_sequences.csv')
    print(eval_df.head(n = 200).to_string())

if __name__ == '__main__':
    main()
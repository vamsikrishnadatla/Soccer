import pandas as pd
import sys
import copy
input_df=''
input_df = pd.read_csv (r"C:\Users\vamsi.krishnadatla\Downloads\sc\soccer.csv")
def Top10Teams(top10_df):
    top10_df = copy.deepcopy(top10_df)
    top10_df.columns = [c.replace(' ', '_') for c in top10_df.columns]
    top10_df['Win_percentage'] = top10_df.apply(lambda row: (row.Wins / row.Games)*100, axis = 1)
    top10_sorted_df=top10_df.sort_values(by=['Win_percentage'],ascending=False,inplace=False).head(10)
    top10_sorted_df=top10_sorted_df['Team']
    top10_sorted_df.to_csv(sys.stdout,index = None,header=False,line_terminator='\n')
    return top10_sorted_df.to_string(index=False)

def smallestdifference(smallest_diff):
    smallest_diff = copy.deepcopy(smallest_diff)
    smallest_diff.columns = [c.replace(' ', '_') for c in smallest_diff.columns]
    smallest_diff['Diff_in_For_against'] = smallest_diff.apply(lambda row: (row.Goals - row.Goals_Allowed), axis = 1)
    diff_sorted_df = smallest_diff.sort_values(by=['Diff_in_For_against'],ascending=True).head(1)
    final_df=diff_sorted_df['Team']
    final_df.to_csv(sys.stdout,index=False,header=False,line_terminator='\n')
    return final_df.to_string(index=False)

def Teamwithmostdraws(most_draws):
    most_draws = copy.deepcopy(most_draws)
    most_draws = most_draws.sort_values(by=['Draws'],ascending=False).head(1)
    most_draws.to_csv(sys.stdout,index=False,line_terminator='\n')
    return most_draws['Team'].to_string(index=False)

Smallest_diff=smallestdifference(input_df)
Top10_teams=Top10Teams(input_df)
Team_with_most_draws=Teamwithmostdraws(input_df)




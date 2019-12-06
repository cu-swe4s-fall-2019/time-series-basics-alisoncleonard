import numpy as np
import pandas as pd
import datetime as dt
from os import listdir
from os.path import isfile
from os.path import join
from functools import reduce


folder = 'smallData/'
files_lst = [f for f in listdir(folder) if isfile(join(folder, f))]

dataframe_list = []

for file in files_lst:
    name = file.split('_')
    df = pd.read_csv(folder+file)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df["time"] = pd.to_datetime(df["time"])
    df.set_index('time', drop=True, inplace=True)
    df.rename(columns={"value": str(name[0])}, inplace=True)
    dataframe_list.append(df)

activity = dataframe_list[0].drop(columns='patient')
activity = activity[activity.activity != '###']
activity = activity[activity.activity != '0+C4218']
activity.activity = activity.activity.astype('float64')

basal = dataframe_list[1].drop(columns='id')
bolus = dataframe_list[2].drop(columns=['Id', ' With meal'])
cgm = dataframe_list[3].drop(columns='Id')
hr = dataframe_list[4].drop(columns='patient')
meal = dataframe_list[5].drop(columns='Id')
smbg = dataframe_list[6].drop(columns='Id')


join = cgm.join([activity, basal, bolus, hr, meal, smbg], how='left')
join.fillna(0, inplace=True)

join.insert(len(join.columns), '15min', join.index.round('15min'))
join.insert(len(join.columns), '5min', join.index.round('5min'))

group_5min = join.groupby('5min').agg({'activity': 'sum', 'bolus': 'sum',
                                       'meal': 'sum', 'smbg': 'mean', 'hr':
                                       'mean', 'cgm': 'mean', 'basal': 'mean'})
group_15min = join.groupby('15min').agg({'activity': 'sum', 'bolus': 'sum',
                                         'meal': 'sum', 'smbg': 'mean', 'hr':
                                         'mean', 'cgm': 'mean', 'basal':
                                         'mean'})

group_5min.to_csv('group_5min.csv', index=True, header=True)
group_15min.to_csv('group_15min.csv', index=True, header=True)

import numpy as np
import pandas as import pd
import datetime as dt


files_lst = [f for f in listdir(folder) if isfile(join(folder, f))]

data_lst = []
for files in files_lst:
    data_lst.append(ImportData(folder+files))


with open(data_csv, 'r') as fhandle:
    reader = csv.DictReader(fhandle)

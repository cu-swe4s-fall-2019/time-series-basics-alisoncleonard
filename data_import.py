import csv
import dateutil.parser
from os import listdir
from os.path import isfile
from os.path import join
import argparse
import datetime
import sys
import numpy as np
from statistics import mean




class ImportData:
    # open file, create a reader from csv.DictReader, and read input times and values

    def __init__(self, data_csv):
        self._time = []
        self._value = []
        self._roundtime = []
        self._roundtimeStr = []
        with open(data_csv, 'r') as fhandle:
            reader = csv.DictReader(fhandle)
            for row in reader:
                try:
                    # parse function converts string 'time' into datetime object
                    self._time.append(dateutil.parser.parse(row['time']))
                except UnicodeDecodeError:
                    print("Remove hidden file from directory, can't process")
                    sys.exit(1)
                except ValueError:
                    print('Bad input format for time')
                    print(row['time'])
                self._value.append(row['value'])
            fhandle.close()


    def linear_search_value(self, key_time):
        # return list of value(s) associated with key_time
        # if none, return -1 and error message
        # value_list = []
        # indices = [i for i, curr in enumerate(self._roundtimeStr) if curr == key_time]
        # print('len _roundtimeStr: ' +str(len(self._roundtimeStr)))
        # print('len _value' + str(len(self._value)))
        # print(indices)
        # if indices == []:
        #     print('invalid time')
        #     return -1
        # for n in indices:
        #     value_list.append(self._value[n])
        # return value_list

        hit = []
        for i in range(len(self._roundtimeStr)):
            if key_time == self._roundtimeStr[i]:
                hit.append(i)
        return hit
        print('invalid time')
        return -1

    def binary_search_value(self,key_time):
        # optional extra credit
        # return list of value(s) associated with key_time
        # if none, return -1 and error message
        pass

    def roundTime(self, resolution, filename):
        # Inputs: obj (ImportData Object) and res (rounding resoultion)
        # objective:
        # create a list of datetime entries and associated values
        # with the times rounded to the nearest rounding resolution (res)
        # ensure no duplicated times
        # handle duplicated values for a single timestamp based on instructions in
        # the assignment
        # return: iterable zip object of the two lists
        # note: you can create additional variables to help with this task
        # which are not returned

        for times in self._time:
            minminus = datetime.timedelta(minutes = (times.minute % resolution))
            minplus = datetime.timedelta(minutes=resolution) - minminus
            if (times.minute % resolution) <= resolution/2:
                newtime = times - minminus
            else: newtime=times + minplus
            self._roundtime.append(newtime)
            self._roundtimeStr.append(newtime.strftime("%m/%d/%Y %H:%M"))
        # find unique times in list
        x = np.array(self._roundtimeStr)
        unique_times = np.unique(x)

        values = []
        for t in unique_times:
            statement = "Non-integers present - can not sum. Check input data in " + str(filename)
            if filename == 'activity_small.csv' or 'bolus_small.csv' or 'meal_small.csv':
                # alert user if non-integer data, removes from any calculations
                try:
                    int_list = [int(i) for i in self.linear_search_value(t)]
                    values.append(sum(int_list))
                except ValueError:
                    print(statement)
                    values.append(statement)
            if filename == 'smbg_small.csv' or 'hr_small.csv' or 'cgm_small.csv':
                try:
                    int_list = [int(i) for i in self.linear_search_value(t)]
                    values.append(mean(int_list))
                except ValueError:
                    print(statement)
                    values.append(statement)
            else:
                try:
                    int_list = [int(i) for i in self.linear_search_value(t)]
                    values.append(int_list)
                except ValueError:
                    print(statement)
                    values.append(statement)

        return zip(unique_times, values)


def printArray(data_list, annotation_list, base_name, key_file):
    # combine and print on the key_file
    # find index with data you want
    base_data = []
    key_idx = 0
    for i in range(len(annotation_list)):
        if annotation_list[i] == key_file:
            base_data = zip(data_list[i]._roundtimeStr, data_list[i]._value)
            print('base data is: ' + annotation_list[i])
            key_idx = i
            break
        if i == len(annotation_list):
            print('Key not found')

    file = open(base_name + '.csv', 'w')
    file.write('time,')

    file.write(annotation_list[key_idx][0:-4]+', ')

    non_key = list(range(len(annotation_list)))
    non_key.remove(key_idx)

    for idx in non_key:
        file.write(annotation_list[idx][0:-4]+', ')
    file.write('\n')


    for time, value in base_data:
        file.write(time+', '+value+', ')
        for n in non_key:
            if time in data_list[n]._roundtimeStr:
                file.write(str(data_list[n].linear_search_value(time))+', ')
            else:
                file.write('0, ')
        file.write('\n')
    file.close()



def main():

    #adding arguments
    parser = argparse.ArgumentParser(description= 'A class to import, combine, and print data from a folder.',
    prog= 'dataImport')

    parser.add_argument('folder_name', type = str, help = 'Name of the folder')

    # parser.add_argument('output_file', type=str, help = 'Name of Output file')
    #
    # parser.add_argument('sort_key', type = str, help = 'File to sort on')
    #
    # parser.add_argument('--number_of_files', type = int,
    # help = "Number of Files", required = False)

    args = parser.parse_args()

    folder_path = args.folder_name
    #pull all the files in the folder
    files_lst = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]


    #import all the files into a list of ImportData objects (in a loop!)
    data_lst = []
    for files in files_lst:
        data_lst.append(ImportData(folder_path+files))

    #create two new lists of zip objects
    # do this in a loop, where you loop through the data_lst
    data_5 = [] # a list with time rounded to 5min
    data_15 = [] # a list with time rounded to 15min


    for file, object in zip(files_lst, data_lst):
        data_5.append(object.roundTime(5, file))

    for file, object in zip(files_lst, data_lst):
        data_5.append(object.roundTime(15, file))

    #print to a csv file
    #printArray(data_5,files_lst,args.output_file+'_5',args.sort_key)
    #printArray(data_15, files_lst,args.output_file+'_15',args.sort_key)

if __name__ == '__main__':
    main()

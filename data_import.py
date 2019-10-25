"""Import csv files containing time series data, round time to desired
increments, and combine data into one files containing all values for that
time.
"""
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
import math


class ImportData:
    """ImportData class reads in data from a csv file using csv.DictReader.
    Time, value data for each file is stored as an individual ImportData
    object.
    """

    # open file, create a reader from csv.DictReader, and read input times
    # and values
    def __init__(self, data_csv):
        """Reads in data from a csv file using csv.DictReader. The python
        module dateutil is used to parse the timestamp string into a
        datetime object.

        Parameters
        -----------
        data_csv - a csv file containing timeseries data

        Returns
        -------
        self._time - a list of all times read from the file
        self._value - a parallel list of all values for each time in self._time
        """
        self._time = []
        self._value = []
        self._roundtime = []
        self._roundtimeStr = []
        with open(data_csv, 'r') as fhandle:
            reader = csv.DictReader(fhandle)
            for row in reader:
                try:
                    # parse converts string 'time' into datetime object
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
        """Find all values in the list self._roundtimeStr for a given
        key time.

        Parameters
        ----------
        self - ImportData object
        key_time - a datetime object used to search through a zipped list

        Returns
        -------
        A list of all values for a given key time.
        """
        # return list of value(s) associated with key_time
        # if none, return -1 and error message

        hit = []
        for i in range(len(self._roundtimeStr)):
            if key_time == self._roundtimeStr[i]:
                hit.append(self._value[i])
        return hit

    def roundTime(self, res, filename):
        """Rounds ImportData object time by a desired resolution to create a
        list of datetime entries and associated values. If a time has multiple
        associated values, either averages or sums the values depending on
        the source data file.

        Parameters
        ----------
        self - ImportData object
        res - An integer interval in minutes to round time by
        filename - An string filename 'abcde.csv' containing the filenames
        of the associated ImportData objects

        Returns
        -------
        A zip object of time, value data from that ImportData object
        """

        for times in self._time:
            minminus = datetime.timedelta(minutes=(times.minute % res))
            minplus = datetime.timedelta(minutes=res) - minminus
            if (times.minute % res) <= res/2:
                newtime = times - minminus
            else:
                newtime = times + minplus
            self._roundtime.append(newtime)
            self._roundtimeStr.append(newtime.strftime("%m/%d/%Y %H:%M"))

        # find unique times in list
        x = np.array(self._roundtimeStr)
        unique_times = np.unique(x)

        values = []
        for t in unique_times:
            statement = "Non-integers, can't sum. Check " + str(filename)
            sum = ['activity_small.csv', 'bolus_small.csv', 'meal_small.csv']
            test_sum = ['test_one.csv']
            # alert user if non-integer data, removes from any calculations
            if filename in sum or test_sum:
                try:
                    int_list = [int(i) for i in self.linear_search_value(t)]
                    values.append(int(math.fsum(int_list)))
                except ValueError:
                    print(statement)
                    values.append(statement)
                except IndexError:  # no value listed for that time
                    continue
            else:
                try:
                    int_list = [int(i) for i in self.linear_search_value(t)]
                    values.append(mean(int_list))
                except ValueError:
                    print(statement)
                    values.append(statement)
                except IndexError:
                    continue
        # wrap zip object in list so that we can iterate through zip objects
        # multiple times
        return list(zip(unique_times, values))


def printArray(data_list, annotation_list, base_name, key_file):
    """Create and save a csv file combining all data from a list of zip
    objects, aligned by times from a given key file.

    Parameters
    ----------
    data_list - a list of zip objects containing time, value pairs, extracted
    from csv files
    annotation_list - a list of files corresponding to the objects in data_list
    base_name - the root name of the outpul csv file
    key_file - a csv file given as a string, specifies what times are used
    to align data from multiple files.

    Returns
    -------
    A csv file saved in the current directory
    """
    # combine and print on the key_file
    # find index with data you want
    # data list is a list of zip objects
    base_data = []
    key_idx = 0
    for i in range(len(annotation_list)):
        if annotation_list[i] == key_file:
            base_data = data_list[i]
            print('base data is: ' + annotation_list[i])
            key_idx = i
            break
        if i == len(annotation_list):
            print('Key not found')

    file = open(base_name + '.csv', 'w')
    file.write('time,')

    file.write(annotation_list[key_idx][0:-4]+', ')

    # non-key is a list of the indices of objects in data_list
    non_key = list(range(len(annotation_list)))
    # remove the index of key file so you don't print that data twice
    non_key.remove(key_idx)

    for idx in non_key:
        file.write(annotation_list[idx][0:-4]+', ')
    file.write('\n')

    # pull data from the values portion of each zip object, for each time

    for time, value in base_data:
        file.write(str(time)+', '+str(value)+', ')
        for n in non_key:
            n_data = data_list[n]
            found = False
            for ntime, nvalue in n_data:
                if str(ntime) == str(time):
                    file.write(str(nvalue)+', ')
                    found = True
                    continue
            if found is False:
                file.write('0, ')
        file.write('\n')
    file.close()


def main():
    """Main function of data_import.py. Imports time series data from csv
    files, rounds data into either 5 or 15 minute increments, and writes a
    csv file containing all the combined data aligned on a specified key file.

    Parameters
    folder_name - a folder inside the current directory that contains to csv
    files to process
    output_file - what to name the output csv file of combined data
    sort_key - a base csv file to align timestamps by
    --number_of_files - an optional argument specifying the number of files to
    process in folder_name

    Returns
    -------
    A csv file containing the aligned data, saved in the current directory
    """

    parser = argparse.ArgumentParser(description='A class to import, combine,'
                                     ' and print data from a folder.',
                                     prog='dataImport')

    parser.add_argument('folder_name', type=str, help='Name of the folder')

    parser.add_argument('output_file', type=str, help='Name of Output file')

    parser.add_argument('sort_key', type=str, help='File to sort on')

    parser.add_argument('--number_of_files', type=int,
                        help="Number of Files", required=False)

    args = parser.parse_args()

    folder = args.folder_name
    # pull all the files in the folder
    files_lst = [f for f in listdir(folder) if isfile(join(folder, f))]

    # import all the files into a list of ImportData objects (in a loop!)
    # made two lists because was overwriting _roundTimeStr
    data_lst_1 = []
    for files in files_lst:
        data_lst_1.append(ImportData(folder+files))

    data_lst_2 = []
    for files in files_lst:
        data_lst_2.append(ImportData(folder+files))

    # create two new lists of zip objects
    # do this in a loop, where you loop through the data_lst
    data_5 = []  # a list with time rounded to 5min
    data_15 = []  # a list with time rounded to 15min

    for file, object in zip(files_lst, data_lst_1):
        data_5.append(object.roundTime(5, file))

    for file, object in zip(files_lst, data_lst_2):
        data_15.append(object.roundTime(15, file))

    # print to a csv file
    printArray(data_5, files_lst, args.output_file+'_5', args.sort_key)
    printArray(data_15, files_lst, args.output_file+'_15', args.sort_key)


if __name__ == '__main__':
    main()

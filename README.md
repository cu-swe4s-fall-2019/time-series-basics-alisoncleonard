# time-series-basics
Time Series basics - importing, cleaning, printing to csv

Note date files are synthetic data.

## Project Description

This software imports time stamped data files, aligns the data based on a key file,
and prints a combined csv file with all the data.

Required modules:
1. data_import.py: main script to import and clean data
2. unittests_data_import.py: unit testing file for data_import.py
3. timeseries_function_tests.py: functional test file using ssshtest framework. Tests that correct output is given when running python data_import.py './smallData/' 'combined_timeseries' 'cgm_small.csv'
4. smallData: folder containing csv files of time series data
5. README.md
6. .travis.yml

## Description of functions

Data_import.py is a script that takes up to 4 arguments to process time series data files.
The arguments for the main function are:
folder_name: a folder inside the current directory that contains to csv files to process
output_file: what to name the output csv file of combined data
sort_key: a base csv file to align timestamps by
--number_of_files: an optional argument specifying the number of files to process in folder_name

Data files read from folder_name are stored as a series of objects in the
ImportData class. This class contains the __init__(self, data_csv) function to read in each
data file as a unique object, the linear_search_value(self, key_time) to generate
a list of values associated with a key time, and roundTime(self, resolution, filename)
which rounds the times based on a specified resolution (example by 5 min intervals).
Depending on the file name, the roundTime function either sums or averages the
values corresponding to the same rounded time.

Outside of the ImportData class, the function printArray(data_list, annotation_list, base_name, key_file)
takes a list of zip objects, a parallel array of corresponding file names, the argparse
argument output_file to specify the output file name, and the argparse argument sort_key
to align the combine output data.

## How to install

1. Ensure that conda is installed in your environment
If `$ conda` gives an error, install conda as required by your operating system

2. Update and configure conda

```
$ conda update --yes conda

$ conda config --add channels bioconda

$ echo ". $HOME/miniconda3/etc/profile.d/conda.sh" >> $HOME/.bashrc
```

3. Install python and required libraries

```
$ conda install --yes python=3.6

$ conda install -y pycodestyle

$ conda install -y python-dateutil

$ conda install -y numpy
```

4. Access software on [GitHub]
(https://github.com/cu-swe4s-fall-2019/time-series-basics-alisoncleonard)

# Homework 11 - Pandas

The file pandas_import.py uses Pandas package to easily clean and align the
data files on the timestamp, round by 5 minute and 15 minute intervals, either
add or average the values for a column with the same rounded timestamp, and
export the dataframes csv files.

## Benchmarking data_import.py vs pandas_import.py

Time to run programs:
data_import.py - 33.05 seconds, 66020 KB memory
pandas_import.py - 11.23 seconds, 77208 KB memory

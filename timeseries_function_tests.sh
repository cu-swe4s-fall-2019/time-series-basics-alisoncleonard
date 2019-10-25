"""
Functional test file for data_import.py script
Uses Stupid Simple (ba)Sh Testing - A functional software testing framwork
"""

#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest
source ssshtest

pycodestyle data_import.py

run test_data_arrays python data_import.py './smallData/' 'combined_timeseries' 'cgm_small.csv'
assert_in_stdout "Bad input format for time

Bad input format for time

Bad input format for time

Bad input format for time

Non-integers, can't sum. Check activity_small.csv
Non-integers, can't sum. Check activity_small.csv
Non-integers, can't sum. Check activity_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check activity_small.csv
Non-integers, can't sum. Check activity_small.csv
Non-integers, can't sum. Check activity_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check basal_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
Non-integers, can't sum. Check bolus_small.csv
base data is: cgm_small.csv
base data is: cgm_small.csv"
assert_no_stderr
assert_exit_code 0

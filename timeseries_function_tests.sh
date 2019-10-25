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
assert_no_stderr
assert_exit_code 0

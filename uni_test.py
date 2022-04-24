from heapq import merge
from tabnanny import check
import unittest
import importlib
csv_combiner = importlib.import_module("csv-combiner")
import pandas as pd
import csv


"""
    A python Script that takes uses UniiTest Library from python to create systematic test cases  
    
    Test Functions
    ----------
    bool test_empty:
        - runs check_csv with empty csv file
        - actual: False, expected False

    bool test_no_args:
        - runs check_csv with no arguments
        - actual: False, expected False
 
    bool test_file_does_not_exist
        - runs check_csv with file that doesn't exist
        - actual: fakse, expected: false

    def test_merge_succesful(self):
        - If I had more time, I would implement testing to ensure valdiation of files transfered
        
        - Given we could be checking if several GB's of CSV files have transfered properly a simple check could be.
           - Counting the # of rows in each CSV processed and comparing to how many rows the merged CSV contains.
        
        - Another set of tests would need to check that the correct values for each columns were passed
           - perhaps taking rows at random from merged csv, and performing validation checks would be the most efficent method. 
    
    Usage:
    ./UniTest.py   
    
"""
class Test_CSV_Merge(unittest.TestCase):

    def test_empty(self):
        actual = csv_combiner.check_csv("fixtures/empty.csv")
        expected = False
        self.assertEqual(actual, expected)

    def test_no_args(self):
        actual = csv_combiner.check_csv("")
        expected = False
        self.assertEqual(actual, expected)
    
    def test_file_does_not_exist(self):
        actual = csv_combiner.check_csv("neverExisted.csv")
        expected = False
        self.assertEqual(actual, expected)
    
 
           

if __name__ == '__main__':
    unittest.main()
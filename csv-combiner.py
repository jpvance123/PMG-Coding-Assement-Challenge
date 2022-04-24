import csv
from distutils.log import error
import os
import sys

"""
    A python Script that takes several CSV files as arguments.  
    Script should output a new CSV file to stdout. 
        - contains the rows from each of the inputs 
        - additional column that has the filename from which the row came (only the file's basename, not the entire path)
        - Use filename as the header for the additional column.
     ...

    Functions
    ----------
    boolean check_csv(argv): 
        - Accepts file paths from command line
        - Checks if more than one file was give
        - File exists
        - File not empty

    merge_files(argv):
        - validates args passed with check_csv
        - if True create files list with paths of CSV files
        - Using CSV python library:
            - For 1st csv file
                - Capture Header
                - Append filename to header
                - Writerow to std.out
                - Then starting with second row write to std.out appending filename as additional column
            - For n consecutive CSV files 
                - Read header so cursor starts with second line
                - for each row in csv file write to std.out
                - continue while i in range of len(files_list)

    Usage:
    ./main.py [CSV Files To Copy...] > [Target CSV File]        
    
"""

def check_csv(argv):
    if (len(argv) <= 1):
        return False
    
    files = argv[1:]

    for path in files:
        if not os.path.exists(path):
            return False
        if os.stat(path).st_size == 0:
            return False
    return True

def merge_files(argv):
    if check_csv(argv):
        files = argv[1:]

        writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)
        
        for i in range(len(files)):
            with open(files[i], 'r', encoding= "utf-8", errors='ignore') as f:
                if(os.path.exists(files[i])):
                    filename = os.path.basename(files[i])
                if(i == 0):
                    reader = csv.reader(f)
                    columns = next(reader)
                    columns += ["filename"]
                    writer.writerow(columns)
                    for row in reader:
                        if row == []:
                            continue
                        
                        row += [filename]
                        writer.writerow(row)
                    f.close()
                else:
                    reader = csv.reader(f)
                    next(reader, None)
                    for row in reader:
                        if row == []:
                            continue
                        
                        row += [filename]
                        writer.writerow(row)
                    f.close()      
    return  
        
    

if __name__ == '__main__':
    args = merge_files(sys.argv)
    
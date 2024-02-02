# The program will find the highest overhead category by percentage.
from pathlib import Path
import csv

# define file path to overheads.csv file
def overhead_function():
    fp = Path.cwd()/"project_group/csv_reports/Overheads.csv"

    # open csv file in read mode
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) #skip header

        # create empty list to store data
        overheads=[] 

        # iterate through each row in the csv file
        for row in reader:
            overheads.append([row[0],float(row[1])]) 

    # define function used as a key for sorting
    def overhead_key(overhead):
        '''
        key parameter to sort cash_list by days
        1 parameter required: profit deficits
        parameter is served as a placeholder
        ''' 
        return -overhead[1]

    # sorted in descending order, key paramter is used to specify a function onto each list
    overheads.sort(key= overhead_key) 

    # format and store highest overhead information
    highest_overhead = f'[HIGHEST OVERHEAD] {overheads[0][0].upper()}: {overheads[0][1]}%\n'

    return highest_overhead



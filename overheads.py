# The program will find the highest overhead category by percentage.
from pathlib import Path
import csv

def overhead_function():
    fp = Path.cwd()/"IGP_PFB/csv_reports/overheads.csv"

    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) #skip header

        overheads=[] 

        for row in reader:
            overheads.append([row[0],float(row[1])]) 
    
    def overhead_key(overhead):
        return -overhead[1]
    
    overheads.sort(key= overhead_key)

    highest_overhead = f'[HIGHEST OVERHEAD] {overheads[0][0].upper()}: {overheads[0][1]}%'

    return highest_overhead



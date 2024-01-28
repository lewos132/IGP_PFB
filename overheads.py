# The program will find the highest overhead category by percentage.
from pathlib import Path
import csv

def overheads():
    fp = Path.cwd()/"IGP_PFB/csv_reports/overheads.csv"

    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        overheads=[] 

        for row in reader:
            overheads.append([row[0],float(row[1])]) 
            
    overheads.sort(key= lambda overhead:-overhead[1])

    highest_overhead = overheads[0]

    return highest_overhead
# Cash-On-Hand csv: The program will firstly compute the
# difference in Cash-on-Hand. If the cash-on-hand is always
# increasing, find out the day and amount the highest
# increment occurs. If the cash-on-hand is always decreasing,
# find out the day and amount the highest decrement occurs. If
# cash-on-hand fluctuates, list down all the days and amount when
# deficit occurs, and find out the top 3 highest deficit amount and the
# days it happened.
from pathlib import Path
import csv

def coh():
    fp = Path.cwd()/"IGP_PFB/csv_reports/cash_on_hand.csv"

    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        cash_on_hand=[] 

        for row in reader:
            cash_on_hand.append([row[0],row[1]]) 

    dailycash = {} # {Day: amount}

    for cashes_on_hand in cash_on_hand: 
        day = int(cashes_on_hand[0])
        cash = float(cashes_on_hand[1])

        if day in dailycash:
            dailycash[day][0] += cash
        else:
            dailycash[day] = [cash]
 
        for key,value in dailycash.items():
            dailycash[day] = [cash]
        
    # create a list to store all the diffs, use .sort() to order them, use splicing to get the first three x[1:4]
    empty_list = []

    for date in range(11, len(dailycash)-1):
        previous_day = date
        current_day = date + 1

        diff = dailycash[current_day][0] - dailycash[previous_day][0]

        empty_list.append((round(diff), current_day)) #[difference, current_day]

    empty_list.sort()

    cash_deficit_top1 = empty_list[0]
    cash_deficit_top2 = empty_list[1]
    cash_deficit_top3 = empty_list[2]

    return cash_deficit_top1, cash_deficit_top2, cash_deficit_top3
print(coh())









    







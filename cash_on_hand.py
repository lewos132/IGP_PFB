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

def coh_function():
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
    cash_list = []

    for date in range(11, len(dailycash)-1):
        previous_day = date
        current_day = date + 1

        diff = dailycash[current_day][0] - dailycash[previous_day][0]

        if diff <0:
            cash_list.append((round(diff), current_day)) #[difference, current_day]
        else:
            pass


    #key parameter to sort by days
    def coh_key(profitdeficits): 
        return profitdeficits[1]
    
    cash_list.sort(key= coh_key)

    output_coh = ''

    for amount, day in cash_list:
        output_coh += f'[CASH DEFICIT] DAY: {day}, AMOUNT: SGD{abs(amount)}\n'

    #sort by descending order of amount
    cash_list.sort()

    for amount, day in cash_list[:1]:
        output_coh += f'[HIGHEST CASH DEFICIT] DAY: {day}, AMOUNT: SGD{abs(amount)}\n'
    
    for amount, day in cash_list[1:2]:
        output_coh += f'[2ND HIGHEST CASH DEFICIT] DAY: {day}, AMOUNT: SGD{abs(amount)}\n'

    for amount, day in cash_list[2:3]:
        output_coh += f'[3RD HIGHEST CASH DEFICIT] DAY: {day}, AMOUNT: SGD{abs(amount)}\n'


    return output_coh










    







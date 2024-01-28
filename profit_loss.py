# The program will firstly compute the
# difference in the net profit column. If the net profit is always
# increasing, find out the day and amount the highest
# increment occurs. If the net profit is always decreasing, find
# out the day and amount the highest decrement occurs. If net
# profit fluctuates, list down all the days and amount when deficit
# occurs, and find out the top 3 highest deficit amount and the days it
# happened.
# day 2 - day 1, day 3 - 2, ...
from pathlib import Path
import csv

def profit_calc():
    fp = Path.cwd()/"IGP_PFB/csv_reports/profit_and_Loss.csv"

    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        ProfitandLoss=[] 

        for row in reader:
            ProfitandLoss.append([row[0],row[4]]) 

    dailyProfit = {} # {Day: amount}

    for ProfitandLosses in ProfitandLoss: 
        day = int(ProfitandLosses[0])
        profit = float(ProfitandLosses[1])

        if day in dailyProfit:
            dailyProfit[day][0] += profit
        else:
            dailyProfit[day] = [profit]


        for key,value in dailyProfit.items():
            dailyProfit[day] = [profit]
        
    # create a list to store all the diffs, use .sort() to order them, use splicing to get the first three x[1:4]
    empty_list = []

    for date in range(11, len(dailyProfit)-1):
        previous_day = date
        current_day = date + 1

        diff = dailyProfit[current_day][0] - dailyProfit[previous_day][0]

        empty_list.append((round(diff), current_day)) #[difference, current_day]

    empty_list.sort()

    profit_deficit_top1 = empty_list[0]
    profit_deficit_top2 = empty_list[1]
    profit_deficit_top3 = empty_list[2]

    return profit_deficit_top1, profit_deficit_top2, profit_deficit_top3











    







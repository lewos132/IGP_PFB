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

def profitloss_function():
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
    profitdeficit_list = []

    for date in range(11, len(dailyProfit)-1):
        previous_day = date
        current_day = date + 1

        diff = dailyProfit[current_day][0] - dailyProfit[previous_day][0]

        if diff < 0:
            profitdeficit_list.append((round(diff), current_day))
        else:
            pass
    
    #key parameter to sort by days
    def profitdeficit_key(profitdeficits): 
        return profitdeficits[1]
    
    #sort by days
    profitdeficit_list.sort(key= profitdeficit_key)

    output_loss = ''

    for amount, day in profitdeficit_list:
        output_loss += f'[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{abs(amount)}\n'

    #sort by descending order of amount
    profitdeficit_list.sort()

    for amount, day in profitdeficit_list[:1]:
        output_loss += f'[HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{abs(amount)}\n'
    
    for amount, day in profitdeficit_list[1:2]:
        output_loss += f'[2ND HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{abs(amount)}\n'

    for amount, day in profitdeficit_list[2:3]:
        output_loss += f'[3RD HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{abs(amount)}\n'

    
    return output_loss













    







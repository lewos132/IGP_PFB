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

# define file path to profit and loss csv file
def profitloss_function():
    fp = Path.cwd()/"IGP_PFB/csv_reports/profit_and_loss.csv"

    # open csv file in read mode
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # create empty list to store data
        ProfitandLoss=[] 

        # iterate through each row in the csv file
        for row in reader:
            ProfitandLoss.append([row[0],row[4]]) 

    # create dictionary to store daily profits
    dailyProfit = {} # {Day: amount}

    # process profit and loss entries
    for ProfitandLosses in ProfitandLoss: 
        day = int(ProfitandLosses[0])
        profit = float(ProfitandLosses[1])

        # accumulate profit for each day
        if day in dailyProfit:
            dailyProfit[day][0] += profit
        else:
            dailyProfit[day] = [profit]

        # update daily profit
        for key,value in dailyProfit.items():
            dailyProfit[day] = [profit]
        
    # create a list to store all the diffs, use .sort() to order them, use splicing to get the first three x[1:4]
    profitdeficit_list = []

    # calculate daily profit differences
    for date in range(11, len(dailyProfit)-1):
        previous_day = date
        current_day = date + 1

        # calculate profit difference between two consecutive days
        diff = dailyProfit[current_day][0] - dailyProfit[previous_day][0]

        # add difference and current day to list
        profitdeficit_list.append((round(diff), current_day))

        # sort list in descending order of profit difference
        profitdeficit_list.sort(reverse=True)

    # identify highest and lowest profit differences
    lowest_value = profitdeficit_list[-1][0] 
    highest_value = profitdeficit_list[0][0]

    deficit_profit_list = [] # temp list to store values if fluctuating

    if highest_value> 0 and lowest_value< 0:
        for deficit in profitdeficit_list:
            if deficit[0] < 0:
                deficit_profit_list.append(deficit)
            else:
                pass
        profitdeficit_list = deficit_profit_list

    else:
        profitdeficit_list.sort()

    output_loss = ''
    if lowest_value >0:
        output_loss += f'[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n'

        for amount, day in profitdeficit_list[:1]:
            output_loss += f'[HIGHEST NET PROFIT SURPLUS] DAY: {day}, AMOUNT: SGD{abs(amount)}\n'

    elif highest_value <0:
        output_loss += f'[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS lower THAN THE PREVIOUS DAY\n'

        for amount, day in profitdeficit_list[:1]:
            output_loss += f'[HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{abs(amount)}\n'

    else:
        def profitdeficit_key(profitdeficits): 
            '''
            key parameter to sort cash_list by days
            1 parameter required: profitdeficits
            parameter is served as a placeholder
            '''
            return profitdeficits[1]
        
        #sort by days
        profitdeficit_list.sort(key= profitdeficit_key)
        
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
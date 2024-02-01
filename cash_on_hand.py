# Cash-On-Hand csv: The program will firstly compute the following 
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

    for cashes_on_hand in cash_on_hand: # iterate through every value of cash_on_hand
        day = int(cashes_on_hand[0]) # assigning the day value
        cash = float(cashes_on_hand[1]) # assigning the cash value

        # add key-value pairs into dailycash dict
        if day in dailycash: 
            dailycash[day][0] += cash
        else:
            dailycash[day] = [cash]
    
        # sets value(cash) assigned to key(day) into a list containing only the value, cash
        for key,value in dailycash.items(): # iterates key-value pairs
            dailycash[day] = [cash]
    
    # created a list to store all the diffs and days
    cash_list = []

    for date in range(11, len(dailycash)-1): # for days starting from 11 to 90
        previous_day = date
        current_day = date + 1

        diff = dailycash[current_day][0] - dailycash[previous_day][0] # calculate differences

        cash_list.append([round(diff), current_day]) # append into as list [diff, current_day]

        #key parameter to sort from highest to lowest
        cash_list.sort(reverse=True)

    # To evaluate whether cash on hand is constantly increasing, decreasing or fluctuating
    lowest_value = cash_list[-1][0] 
    highest_value = cash_list[0][0]

    deficit_cash_list = [] # temp list to store values if fluctuating

    if highest_value> 0 and lowest_value< 0: # for scenario where differences fluctates
        for deficit in cash_list: # iterates through every value
            if deficit[0] < 0: # if difference less than 0
                deficit_cash_list.append(deficit) 
            else:
                pass # to only get the days where there's deficit
        cash_list = deficit_cash_list # assigning temp list to cash_list

    else: # for scenarios where always increasing or decreasing
        cash_list.sort()

        
    output_coh = '' # empty string 

    if lowest_value >0:
        output_coh += f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n' # add in days where cash surplus occurs 
        

        for amount, day in cash_list[:1]:
            output_coh += f'[HIGHEST CASH SURPLUS] DAY: {day}, AMOUNT: SGD{abs(amount)}\n'

    elif highest_value <0:
        output_coh += f'[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\n' # add in days where cash deficit occurs 

        for amount, day in cash_list[:1]:
            output_coh += f'[HIGHEST CASH DEFICIT] DAY: {day}, AMOUNT: SGD{abs(amount)}\n'

    else:
        def coh_key(cashdeficits): 
            '''
            key parameter to sort cash_list by days
            1 parameter required: profit deficits
            parameter is served as a placeholder
            '''
            return cashdeficits[1]
        
        cash_list.sort(key= coh_key) # sort by day in ascending order, key paramter is used to specify a function onto each list

        for amount, day in cash_list:
            output_coh += f'[CASH DEFICIT] DAY: {day}, AMOUNT: SGD{abs(amount)}\n' # add in days where cash deficit occurs 

        #sort by descending order of amount
        cash_list.sort()

        for amount, day in cash_list[:1]:
            output_coh += f'[HIGHEST CASH DEFICIT] DAY: {day}, AMOUNT: SGD{abs(amount)}\n'
        
        for amount, day in cash_list[1:2]:
            output_coh += f'[2ND HIGHEST CASH DEFICIT] DAY: {day}, AMOUNT: SGD{abs(amount)}\n'

        for amount, day in cash_list[2:3]:
            output_coh += f'[3RD HIGHEST CASH DEFICIT] DAY: {day}, AMOUNT: SGD{abs(amount)}\n'


    return output_coh

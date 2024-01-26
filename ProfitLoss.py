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
    fp = Path.cwd()/"csv_reports/daily_revenue.csv"

    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # create an empty list for delivery record
        ProfitandLoss=[] 

        # append delivery record into the deliveryRecords list
        for row in reader:
            ProfitandLoss.append([row[0],row[1]]) 

    dailyReveneue = {} # [Day: amount]

    for ProfitandLosses in ProfitandLoss: 
        day = int(ProfitandLosses[0])
        rev = float(ProfitandLosses[1])


        if day in dailyReveneue:
            dailyReveneue[day][0] += rev
        else:
            dailyReveneue[day] = [rev]

    # print(dailyReveneue)
        for key,value in dailyReveneue.items():
            dailyReveneue[day] = [rev]
        # print(dailyReveneue)
    # create a lsot to store all the diffs, use .sort() to order them, use splicing to get the first three x[1:4]
    empty_list = []

    for i in range(1, len(dailyReveneue)-1):
        key1 = i
        key2 = i + 1
        # print(key2)
        diff = dailyReveneue[key2][0] - dailyReveneue[key1][0]
        empty_list.append((round(diff, 2), key1, key2)) 
        # print(round(diff, 2))

    # print(empty_list)
    empty_list.sort()
    # print(empty_list)

    top_loss = empty_list[0]
    top_increase = empty_list[-1]
    print(f' top increase is {top_increase[0]} on days {top_increase[1]} and {top_increase[2]}, top loss is {top_loss[0]}')


profit_calc()
print("hehehehaw")





    # print(key2)
    # print(key1)
    # diff = dailyReveneue[key2] - dailyReveneue[key1]
    # dict_value = dailyReveneue[i]
    # print(diff)

        # diff = dailyReveneue[i+2] - dailyReveneue[i+1]


# for i in range(len(dailyReveneue- 1)):
    # pass
#     print(sorted_revenue[i])
# for i in range(len(keys) - 1):
#     key1 = keys[i]
#     key2 = keys[i + 1]
    
#     diff = dailyReveneue[key2] - dailyReveneue[key1]
    
#     print(f"Difference between {key1} and {key2}: {diff}")



# sorted_list = sorted(list(dailyReveneue))
# highest_revenue = 0.0
# for day in sorted_list:
#     key1 = sorted_list[day]
#     #key2 = sorted_list[day+1]

#     print(key1)
    
    #diff = dailyReveneue[key2] - dailyReveneue[key1]

    #print(f'diff is {diff}')


    







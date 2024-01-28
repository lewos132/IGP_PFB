import profit_loss
from pathlib import Path


profit_deficit_top1 = profit_loss.profit_calc()[0]
profit_deficit_top2 = profit_loss.profit_calc()[1]
profit_deficit_top3 = profit_loss.profit_calc()[1]

# cash_deficit_top1 =
# cash_deficit_top2 = 
# cash_deficit_top3 =


out_summary = Path.cwd()/'IGP_PFB/paymentSummary.txt' # ouput to .txt file 

# write information onto .txt file, 'UTF-8' to be able to represent any unicode character set 
with out_summary.open(mode="w", encoding="UTF-8") as file: 
    # title in .txt file
    file.write('PowerLeopard Payment Summary')
    file.write('\n===============================')
    file.write('\nDriver ID, Total Sales, Total Earning, Sales to Earnings Ratio')
    file.write(f'\n{abs(profit_deficit_top1[0])}')



    
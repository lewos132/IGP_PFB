import profit_loss, cash_on_hand, overheads
from pathlib import Path

out_summary = Path.cwd()/'IGP_PFB/paymentSummary.txt' # ouput to .txt file 

# write information onto .txt file, 'UTF-8' to be able to represent any unicode character set 
with out_summary.open(mode="w", encoding="UTF-8") as file: 
    file.write(f'{profit_loss.profitloss_function()}')
    file.write(f'{cash_on_hand.coh_function()}')
    file.write(f'{overheads.overhead_function()}')
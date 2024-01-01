
from cmath import inf


def buy_sell(prices): 

    total_min, total_max = float(inf), 0
    
    for price in prices: 
        max_profit = price - total_min
        total_max = max(max_profit, total_max)
        total_min = min(total_min, price)
    return max_profit


prices = [310,315,275,295,260,270,290,230,255,250]
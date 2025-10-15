arr = [4,5,3,7,2,8]

def best_stock_sell(price):
    min_price= price[0]
    max_profit =0
    
    for p in price:
        min_price = min(min_price,p)
        profit = p - min_price
        max_profit = max(max_profit,profit)
    return max_profit

print(best_stock_sell(arr))
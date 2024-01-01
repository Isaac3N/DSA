

def best_sell_stock(stocks):
    n = len(stocks)
    l, r = 0, 1
    best_time = []
    largest_profit = 0

    while l < r and r < n:

        difference = stocks[r] - stocks[l]

        if difference > 0:
            if difference > largest_profit:
                largest_profit = difference
                if best_time:
                    best_time.pop()

                best_time.append([stocks[l], stocks[r]])
            r += 1

        elif difference < 0:
            l = r
            r += 1

        else:
            return []

    return best_time


stocks = [2, 3, 1, 5, 2]

print(best_sell_stock(stocks))

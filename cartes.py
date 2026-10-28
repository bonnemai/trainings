def u(n): 
    return 2 if n==0 else u(n-1)+n+2*(n+1)

for i in range(100):
    print(i, u(i))
#   StockPriceTracker: A class to track stock prices over time.
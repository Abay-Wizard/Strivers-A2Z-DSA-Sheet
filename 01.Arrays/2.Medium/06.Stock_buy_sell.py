# Problem: best time to buy and sell stock, you are essentially required to find the maxiumum possible profit

def buy_sell_stock(arr):
    n=len(arr)
    profit=0
    miniCost=arr[0]
    for i in range(1,n):
        cost=arr[i]-miniCost
        profit=max(profit,cost)
        miniCost=min(miniCost,arr[i])
        
    return profit
print(buy_sell_stock([7,1,5,3,6,4]))
print(buy_sell_stock([7,6,4,3,1]))
        
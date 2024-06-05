# Write a program that efficiently determines the minimum number of coins needed to make a given amount of change.

def coin_exchange(coins,amount):
    list = [float('inf')] * (amount+1)
    print("initial list will be",list)
    list[0] = 0
    
    for coin in coins:
        for x in range(coin ,amount+1):
            list[x] = min(list[x] ,  list[x-coin] +1)
    print("final list::",list)
    return list[amount]

coins = [1, 2, 5]
x = 34
print(coin_exchange(coins,x))
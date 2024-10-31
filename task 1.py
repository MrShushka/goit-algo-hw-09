import timeit

# Жадібний алгоритм 
def find_coins_greedy(amount):
    
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count
            
    return result

# Алгоритм динамічного програмування 
def find_min_coins(amount):

    coins = [1, 2, 5, 10, 25, 50]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  
    

    coin_used = [0] * (amount + 1)
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i] > dp[i - coin] + 1:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin
    
    return result

amount = 113

greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=1000)
greedy_result = find_coins_greedy(amount)
print("Жадібний алгоритм:", greedy_result)
print("Час виконання жадібного алгоритму:", greedy_time, "секунд")

dp_time = timeit.timeit(lambda: find_min_coins(amount), number=1000)
dp_result = find_min_coins(amount)
print("Динамічне програмування:", dp_result)
print("Час виконання алгоритму динамічного програмування:", dp_time, "секунд")
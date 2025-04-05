
# memeoization 

# striver repr 
# simopplest represenattion 

def f(dp,arr,  i, buy):
    
    if i == len(arr):
        return 0  # Base case: If we have reached the end of the array, return zero profit
    
    if dp[i][buy] != -1:
        return dp[i][buy] 
    
    profit = 0
    
    if buy == 1 :
        profit = max(0 + f(dp,arr,  i + 1, 1), -arr[i] + f(dp,arr,  i + 1, 0 ))
    else:
        profit = max(0 + f(dp,arr,  i + 1, 0), arr[i] + f(dp,arr,  i + 1, 1))
    
    dp[i][buy] = profit  
    return profit

if __name__ == "__main__":
    n = 6
    arr = [7, 1, 5, 3, 6, 4]
    dp = [[-1 for _ in range(2)] for _ in range(n)]
    
    # edge case  
    if n == 0:
        print(0)
    
    max_profit = f(dp,arr,  0, 1)
    print(" maximum profit that can be generated  ", max_profit)



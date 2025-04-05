def unbounded_knapsack(n, W, val, wt):
    # Create a DP table initialized with 0
    dp = [[0] * (W + 1) for _ in range(n)]
    
    # Base Condition
    for i in range(0, W + 1):
        dp[0][i] = (i // wt[0]) * val[0]  # Compute max value for first item
    
    # Fill the DP table
    
    # for i in range(wt[0], W + 1): also rep 
    for ind in range(1, n):
        for cap in range(W + 1):
            not_taken = dp[ind - 1][cap]  # Max value without taking current item
            
            taken = float('-inf')  # Equivalent to INT_MIN
            if wt[ind] <= cap:
                taken = val[ind] + dp[ind][cap - wt[ind]]  # Max value including current item
            
            dp[ind][cap] = max(not_taken, taken)  # Store the best value
    
    return dp[n - 1][W]  # Return the max value at full capacity

# Example usage
wt = [2, 4, 6]  # Weights of items
val = [5, 11, 13]  # Values of items
W = 10  # Knapsack capacity
n = len(wt)  # Number of items

print("The Maximum value of items the thief can steal is", unbounded_knapsack(n, W, val, wt))

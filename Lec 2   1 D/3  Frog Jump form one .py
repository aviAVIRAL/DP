




# recurrences 

def f(ind):
    if ind == 0:
        return 0

    jumpOne = f(ind - 1) + abs(arr[ind] - arr[ind - 1])

    jumpTwo = float('inf')  
    # 
    if ind > 1: #     if  ind >=2 :     also
        jumpTwo = f(ind - 2) + abs(arr[ind] - arr[ind - 2])

    return min(jumpOne, jumpTwo)

if __name__ == "__main__":
    arr = [30, 10, 60, 10, 60, 50]
    n = len(arr)
    print(f(n - 1))


print()

# memo sriver erp 

def f(ind):
    if ind == 0:
        return 0
    
    if dp[ind] != -1:
        return dp[ind]
    
    jumpOne = f(ind-1) + abs(height[ind] - height[ind-1])
    jumpTwo = 1000
    if ind > 1:
        jumpTwo = f(ind-2) + abs(height[ind] - height[ind-2])
    
    dp[ind] = min(jumpOne, jumpTwo)
    
    return dp[ind]

if __name__ == "__main__":
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    dp = [-1] * n
    print(f(n-1))


# memozation proper represent 

def f(ind, dp):
    if ind == 0:
        return 0
    
    if dp[ind] != -1:
        return dp[ind]
    
    jumpOne = f(ind-1, dp) + abs(height[ind] - height[ind-1])
    jumpTwo = 1000

    if ind > 1:
        jumpTwo = f(ind-2, dp) + abs(height[ind] - height[ind-2])
    
    dp[ind] = min(jumpOne, jumpTwo)
    
    return dp[ind]

if __name__ == "__main__":
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    dp = [-1] * n
    print(f(n-1, dp))

print()

# tabulation  
def tabulation(height):
    n = len(height)
    dp = [0] * n  # Initialize dp array with 0 for all indices
    
    # Base case
    dp[0] = 0  # The cost to reach the first step is 0
    
    # Fill the dp table iteratively
    for i in range(1, n):
        # Calculate jumpOne (from the previous step)
        jumpOne = dp[i - 1] + abs(height[i] - height[i - 1])
        
        # Calculate jumpTwo (from two steps back) if possible
        jumpTwo = float('inf')
        if i > 1:
            jumpTwo = dp[i - 2] + abs(height[i] - height[i - 2])
        
        # Take the minimum cost to reach the current step
        dp[i] = min(jumpOne, jumpTwo)
    
    # The answer is the cost to reach the last step
    return dp[-1]

if __name__ == "__main__":
    height = [30, 10, 60, 10, 60, 50]
    print(tabulation(height))


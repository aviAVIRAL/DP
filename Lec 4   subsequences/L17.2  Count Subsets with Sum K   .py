
# tabulation  

def findWays(num, k):
    n = len(num)
    
    # Initialize a 2D DP array to store the count of subsets for different targets.
    dp = [[0] * (k + 1) for _ in range(n)]
    
    # Base case: There is always one way to make a subset with a target sum of 0 (empty subset).
    for i in range(n):
        dp[i][0] = 1
    
    # Handle the base case for the first element in the array.
    if num[0] <= k:
        dp[0][num[0]] = 1

    # Iterate through the elements in the array.
    for ind in range(1, n):
        for target in range(1, k + 1):
            # If the current element is not taken, the count is the same as the previous row.
            notTaken = dp[ind - 1][target]
            
            # If the current element is taken, subtract its value from the target and check the previous row.
            taken = 0
            if num[ind] <= target:
                taken = dp[ind - 1][target - num[ind]]
            
            # Update the DP array with the total count of ways (taken + notTaken).
            dp[ind][target] = notTaken + taken

    # The result is stored in the bottom-right cell of the DP array.
    return dp[n - 1][k]

def main():
    arr = [1, 2, 2, 3]
    k = 3
    
    # Find and print the number of subsets that can be formed with a sum of 'k'.
    print("The number of subsets found are", findWays(arr, k))

if __name__ == "__main__":
    main()




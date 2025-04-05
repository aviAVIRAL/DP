

def subsetSumUtil(ind, target, arr, dp):
    # Base case: If the target sum is 0, we have found a subset that sums to the target.
    if target == 0:
        return True
    
    # Base case: If we have reached the first element of the array, check if it equals the target.
    if ind == 0:
        return arr[0] == target
    
    # Check if the result for this combination of 'ind' and 'target' has already been computed.
    if dp[ind][target] != -1:
        return dp[ind][target]
    
    # Recursive cases:
    # 1. Try not taking the current element.
    notTaken = subsetSumUtil(ind - 1, target, arr, dp)
    
    # 2. Try taking the current element if it is less than or equal to the target.
    taken = False
    if arr[ind] <= target:
        taken = subsetSumUtil(ind - 1, target - arr[ind], arr, dp)
        
    # Update the DP table and return the result.
    dp[ind][target] = notTaken or taken
    return dp[ind][target]

def canPartition(n, arr):
    # Calculate the total sum of the array elements.
    totSum = sum(arr)
    
    # If the total sum is odd, it cannot be partitioned into two equal subsets.
    if totSum % 2 == 1:
        return False
    else:
        # Calculate the target sum for each subset.
        k = totSum // 2
        
        # Initialize a memoization table for dynamic programming.
        dp = [[-1 for i in range(k + 1)] for j in range(n)]
        
        # Call the subsetSumUtil function to check if a subset with sum 'k' exists.
        return subsetSumUtil(n - 1, k, arr, dp)

def main():
    arr = [2, 3, 3, 3, 4, 5]
    n = len(arr)
    
    # Check if the array can be partitioned into two equal subsets and print the result.
    if canPartition(n, arr):
        print("The Array can be partitioned into two equal subsets")
    else:
        print("The Array cannot be partitioned into two equal subsets")

if __name__ == "__main__":
    main()




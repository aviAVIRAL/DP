

def countPartitionsUtil(ind, target, arr, dp):
    # Base case: If we have reached the first element in the array.
    if ind == 0:
        # Check if the target is zero and the first element is also zero, in which case there are two possibilities.
        if target == 0 and arr[0] == 0:
            return 2
        # If the target is equal to the first element, there is one possibility.
        if target == 0 or target == arr[0]:
            return 1
        # Otherwise, there is no valid partition.
        return 0

    # If the result for this state is already calculated, return it.
    if dp[ind][target] != -1:
        return dp[ind][target]

    # Calculate the number of possibilities when the current element is not taken.
    notTaken = countPartitionsUtil(ind - 1, target, arr, dp)
    
    # Initialize a variable for the number of possibilities when the current element is taken.
    taken = 0
    if arr[ind] <= target:
        taken = countPartitionsUtil(ind - 1, target - arr[ind], arr, dp)

    # Store the total number of possibilities in the DP table.
    dp[ind][target] = notTaken + taken
    return dp[ind][target]

def targetSum(n, target, arr):
    totSum = 0
    for i in range(len(arr)):
        totSum += arr[i]

    # Checking for edge cases
    if totSum - target < 0:
        return 0
    if (totSum - target) % 2 == 1:
        return 0

    s2 = (totSum - target) // 2

    dp = [[-1 for j in range(s2 + 1)] for i in range(n)]
    return countPartitionsUtil(n - 1, s2, arr, dp)

def main():
    arr = [1, 2, 3, 1]
    target = 3
    n = len(arr)
    print("The number of ways found is", targetSum(n, target, arr))

if __name__ == '__main__':
    main()






# tabul

def minimumElements(arr, T):
    n = len(arr)
    # Initialize a DP table with 0 values for bottom-up dynamic programming.
    dp = [[0 for _ in range(T + 1)] for _ in range(n)]

    # Fill in the DP table for the first element in the array (base case).
    for i in range(T + 1):
        if i % arr[0] == 0:
            dp[0][i] = i // arr[0]
        else:
            # Set an initial large value to indicate that it's not possible to achieve the target sum.
            dp[0][i] = int(1e9)

    # Iterate over the array elements and target values to fill in the DP table.
    for ind in range(1, n):
        for target in range(T + 1):
            # Calculate the minimum number of elements needed to achieve the current target.
            notTake = dp[ind - 1][target]  # Option: Don't take the current element.
            take = int(1e9)  # Initialize as a large value.
            if arr[ind] <= target:
                # Option: Take the current element, reduce the target, and add 1 to the count.
                take = 1 + dp[ind][target - arr[ind]]
            # Store the minimum of the two options in the DP table.
            dp[ind][target] = min(notTake, take)

    # The result is stored in the last cell of the DP table.
    ans = dp[n - 1][T]
    # If the result is still equal to a very large value, it means it's not possible to achieve the target sum.
    if ans >= int(1e9):
        return -1
    return ans

def main():
    arr = [1, 2, 3]
    T = 7    
    print("The minimum number of coins required to form the target sum is", minimumElements(arr, T))

if __name__ == "__main__":
    main()


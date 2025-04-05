
# mem 

def minimumElementsUtil(arr, ind, T, dp):
    # Base case: If we have reached the first element in the array.
    if ind == 0:
        # If the target T is divisible by the first element, return the quotient as the minimum number of coins.
        if T % arr[0] == 0:
            return T // arr[0]
        else:
            # If not, it's not possible to achieve the target sum, so return a very large value.
            return int(1e9)

    # If the result for this state is already calculated, return it.
    if dp[ind][T] != -1:
        return dp[ind][T]

    # Initialize variables for cases when we don't take the current element.
    notTaken = 0 + minimumElementsUtil(arr, ind - 1, T, dp)

    # Initialize a variable for the case when we take the current element.
    taken = int(1e9)

    # Check if the current element can be used to reduce the target sum.
    if arr[ind] <= T:
        taken = 1 + minimumElementsUtil(arr, ind, T - arr[ind], dp)

    # Store the minimum of the two cases in the DP table.
    dp[ind][T] = min(notTaken, taken)
    return dp[ind][T]

def minimumElements(arr, T):
    n = len(arr)
    # Initialize a DP table with -1 values.
    dp = [[-1 for j in range(T + 1)] for i in range(n)]
    # Calculate the minimum number of coins required using the helper function.
    ans = minimumElementsUtil(arr, n - 1, T, dp)

    # If the result is still equal to a very large value, it means it's not possible to achieve the target sum.
    if ans >= int(1e9):
        return -1
    return ans

def main():
    arr = [1, 2, 3]
    T = 7
    print("The minimum number of coins required to form the target sum is", minimumElements(arr, T))

if __name__ == '__main__':
    main()


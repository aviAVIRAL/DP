

def is_palindrome(i, j, s):
    # Helper function to check if a substring s[i...j] is a palindrome
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def palindrome_partitioning(s):
    # Main function to find the minimum number of partitions
    n = len(s)
    dp = [0] * (n + 1)
    dp[n] = 0  # Initialize the last element of dp to 0
    for i in range(n - 1, -1, -1):  # Start from the second-to-last element and move backward
        min_cost = float('inf')
        # Iterate over possible sub strings starting from index i
        for j in range(i, n):
            if is_palindrome(i, j, s):
                # If s[i...j] is a palindrome, calculate the cost
                cost = 1 + dp[j + 1]
                min_cost = min(min_cost, cost)
        dp[i] = min_cost

    return dp[0] - 1  # Subtract 1 to exclude the initial unpartitioned string

if __name__ == "__main__":
    str = "BABABCBADCEDE"
    partitions = palindrome_partitioning(str)
    print("The minimum number of partitions:", partitions)



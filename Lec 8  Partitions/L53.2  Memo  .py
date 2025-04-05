

def is_palindrome(i, j, s):
    # Helper function to check if a substring s[i...j] is a palindrome
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def f(i, n, s, dp):
    # Base case: If we reach the end of the string, no further partition is needed
    if i == n:
        return 0

    if dp[i] != -1:
        return dp[i]
    
    min_cost = float('inf')
    
    # Iterate over possible substrings starting from index i
    for j in range(i, n):
        if is_palindrome(i, j, s):
            # If s[i...j] is a palindrome, calculate the cost
            cost = 1 + f(j + 1, n, s, dp)
            min_cost = min(min_cost, cost)

    dp[i] = min_cost
    return dp[i]

def palindrome_partitioning(s):
    # Main function to find the minimum number of partitions
    n = len(s)
    dp = [-1] * n  # Initialize a memoization array with -1
    return f(0, n, s, dp) - 1  # Subtract 1 to exclude the initial unpartitioned string

if __name__ == "__main__":
    str = "BABABCBADCEDE"
    partitions = palindrome_partitioning(str)
    print("The minimum number of partitions:", partitions)



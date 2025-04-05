

print()





# Function to solve the problem using dynamic programming
def solveUtil(n, arr, dp):
    # Initialize the first element of the DP table with the first element of the array
    dp[0] = arr[0]
    
    # Loop through the array starting from the second element
    for i in range(1, n):
        # Calculate the maximum value when picking the current element
        pick = arr[i]
        
        # Check if there are at least two elements before the current element
        if i > 1:
            pick += dp[i - 2]
        
        # Calculate the maximum value when not picking the current element
        non_pick = 0 + dp[i - 1]
        
        # Store the maximum of the two choices in the DP table
        dp[i] = max(pick, non_pick)
    
    # Return the maximum value for the last index
    return dp[n - 1]

# Function to solve the problem for the given array
def solve(n, arr):
    # Initialize a DP table with -1 values to store intermediate results
    dp = [-1 for _ in range(n)]
    
    # Call the solveUtil function to find the maximum value
    return solveUtil(n, arr, dp)

# Main function to test the code
def main():
    arr = [2, 1, 4, 9]
    n = len(arr)
    
    # Call the solve function and print the result
    print(solve(n, arr))

if __name__ == '__main__':
    main()

print("......")

# Function to solve the problem using dynamic programming
def solveUtil(n, arr, dp):
    # Initialize the first element of the DP table with the first element of the array
    dp[0] = arr[0]
    
    # Loop through the array starting from the second element
    for i in range(1, n):
        # Calculate the maximum value when picking the current element
        
        # Check if there are at least two elements before the current element
        if i > 1:
            pick += dp[i - 2]
        else :
            pick = arr[i]
        
        # Calculate the maximum value when not picking the current element
        non_pick = 0 + dp[i - 1]
        
        # Store the maximum of the two choices in the DP table
        dp[i] = max(pick, non_pick)
    
    # Return the maximum value for the last index
    return dp[n - 1]

# Function to solve the problem for the given array
def solve(n, arr):
    # Initialize a DP table with -1 values to store intermediate results
    dp = [-1 for _ in range(n)]
    
    # Call the solveUtil function to find the maximum value
    return solveUtil(n, arr, dp)

# Main function to test the code
def main():
    arr = [2, 1, 4, 9]
    n = len(arr)
    
    # Call the solve function and print the result
    print(solve(n, arr))

if __name__ == '__main__':
    main()


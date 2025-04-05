# tabulation 



import sys

# Function to find the maximum path sum in the matrix
def getMaxPathSum(matrix):
    n = len(matrix)  # Number of rows
    m = len(matrix[0])  # Number of columns
    
    # Initialize a dynamic programming table (dp) with zeros
    dp = [[0 for j in range(m)] for i in range(n)]
    
    # Initializing the first row of dp as the base condition
    for j in range(m):
        dp[0][j] = matrix[0][j]
    
    # Iterate through the matrix to compute the maximum path sum
    for i in range(1, n):
        for j in range(m):
            # Calculate the three possible moves: up, left diagonal, and right diagonal
            up = matrix[i][j] + dp[i - 1][j]
            
            # Handle left diagonal
            left_diagonal = matrix[i][j]
            if j - 1 >= 0:
                left_diagonal += dp[i - 1][j - 1]
            else:
                left_diagonal += -int(1e9)  # A large negative value if out of bounds
            
            # Handle right diagonal
            right_diagonal = matrix[i][j]
            if j + 1 < m:
                right_diagonal += dp[i - 1][j + 1]
            else:
                right_diagonal += -int(1e9)  # A large negative value if out of bounds
            
            # Store the maximum of the three moves in dp
            dp[i][j] = max(up, left_diagonal, right_diagonal)
    
    # Find the maximum path sum in the last row of dp
    maxi = -sys.maxsize
    for j in range(m):
        maxi = max(maxi, dp[n - 1][j])
    
    return maxi  # Return the maximum path sum

def main():
    # Define the input matrix
    matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
    
    # Call the getMaxPathSum function and print the result
    print(getMaxPathSum(matrix))

if __name__ == "__main__":
    main()




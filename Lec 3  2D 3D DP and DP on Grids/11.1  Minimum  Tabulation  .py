

# tabu lation 

def minimum_path_sum(triangle, n):
    # Create a 2D array dp to store minimum path sums
    dp = [[0 for j in range(n)] for i in range(n)]
    
    # Initialize the bottom row of dp with the values from the last row of the triangle
    for j in range(n):
        dp[n - 1][j] = triangle[n - 1][j]
    
    # Start from the second-to-last row and work upwards
    for i in range(n - 2, -1, -1):
        for j in range(i, -1, -1):
            # Calculate the minimum path sum for the current cell by considering two possible moves: down and diagonal
            down = triangle[i][j] + dp[i + 1][j]
            diagonal = triangle[i][j] + dp[i + 1][j + 1]
            
            # Store the minimum of the two possible moves in dp
            dp[i][j] = min(down, diagonal)
    
    # The minimum path sum will be stored in dp[0][0] after the loops
    return dp[0][0]

def main():
    # Define the input triangle and its size
    triangle = [[1], [2, 3], [3, 6, 7], [8, 9, 6, 10]]
    n = len(triangle)
    
    # Call the minimum_path_sum function and print the result
    print(minimum_path_sum(triangle, n))

if __name__ == '__main__':
    main()


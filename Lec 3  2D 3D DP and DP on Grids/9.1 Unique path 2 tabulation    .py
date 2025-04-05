
# tabulation 

def mazeObstacles(n, m, maze):
    # Create a DP table initialized with 0 values.
    dp = [[0 for _ in range(m)] for _ in range(n)]


    for i in range(n):
        for j in range(m):
            if (i  ==0 and j == 0 ): dp[i][j] = 1 
            elif  maze[i][j] == -1: dp[i][j] = 0 # impo 
            else:
                up = 0 
                left= 0 
                if i > 0:  # Add paths from the cell above.
                    up += dp[i - 1][j]
                if j > 0:  # Add paths from the cell to the left.
                    left += dp[i][j - 1]
                dp[i][j]=up + left    # The bottom-right corner contains the total number of unique paths.
    return dp[n - 1][m - 1]

def main():
    maze = [[0, 0, 0], [0, -1, 0], [0, 0, 0]]
    n = len(maze)
    m = len(maze[0])
    print(mazeObstacles(n, m, maze))

if __name__ == '__main__':
    main()


# also repr by vhate gpt  


def mazeObstacles(n, m, maze):
    # Create a DP table initialized with 0 values.
    dp = [[0 for _ in range(m)] for _ in range(n)]

    # # Initialize the base case.
    # if maze[0][0] != -1:
    #     dp[0][0] = 1 
    # else: 
    #     dp[0][0] = 0

    # Fill the DP table iteratively.
    for i in range(n):
        for j in range(m):
            if (i  ==0 and j == 0 ): dp[i][j] = 1 
            elif  maze[i][j] == -1: dp[i][j] = 0 # impo 
            else:
                if i > 0:  # Add paths from the cell above.
                    dp[i][j] += dp[i - 1][j]
                if j > 0:  # Add paths from the cell to the left.
                    dp[i][j] += dp[i][j - 1]

    # The bottom-right corner contains the total number of unique paths.
    return dp[n - 1][m - 1]

def main():
    maze = [[0, 0, 0], [0, -1, 0], [0, 0, 0]]
    n = len(maze)
    m = len(maze[0])
    print(mazeObstacles(n, m, maze))

if __name__ == '__main__':
    main()

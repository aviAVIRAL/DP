# memorization 

def mazeObstaclesUtil(i, j, maze, dp):

    if i < 0 or j < 0 or maze[i][j] == -1:
        return 0

# # also rep 
#     if i < 0 or j < 0 :
#         return 0

#     if maze[i][j] == -1:
#         return 0

    if i == 0 and j == 0:
        return 1

    if dp[i][j] != -1:
        return dp[i][j]

    up = mazeObstaclesUtil(i - 1, j, maze, dp)
    left = mazeObstaclesUtil(i, j - 1, maze, dp)

    dp[i][j] = up + left
    return dp[i][j]

def mazeObstacles(n, m, maze):
    dp = [[-1 for j in range(m)] for i in range(n)]
    return mazeObstaclesUtil(n - 1, m - 1, maze, dp)

def main():
    maze = [[0, 0, 0], [0, -1, 0], [0, 0, 0]]
    n = len(maze)
    m = len(maze[0])

    print(mazeObstacles(n, m, maze))

if __name__ == '__main__':
    main()




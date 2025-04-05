

# Minimum cost to cut the stick| (DP-50)


def min_cost(n, c, cuts):
    # Define a 2D memoization table to store intermediate results
    dp = [[0] * (c + 2) for _ in range(c + 2)]

    # Extend the cuts list with 0 and n, and sort it
    cuts = [0] + cuts + [n]
    cuts.sort()

    # Fill the memoization table using dynamic programming
    for length in range(2, c + 3):
        for i in range(c + 3 - length):
            j = i + length - 1
            dp[i][j] = float('inf')

            # Find the optimal partition point and calculate the cost
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + (cuts[j] - cuts[i]))

    # The result is stored in the top-right corner of the memoization table
    return dp[0][c + 1]

if __name__ == "__main__":
    cuts = [3, 5, 1, 4]
    c = len(cuts)
    n = 7

    print("The minimum cost incurred:", min_cost(n, c, cuts))











def min_cost(n, c, cuts):
    # Define a 2D memoization table to store intermediate results
    dp = [[-1] * (c + 1) for _ in range(c + 1)]

    # Extend the cuts list with 0 and n, and sort it
    cuts = [0] + cuts + [n]
    cuts.sort()

    # Recursive function to find the minimum cost
    def f(i, j):
        # Base case
        if i > j:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        mini = float('inf')
        
        for ind in range(i, j + 1):
            ans = cuts[j + 1] - cuts[i - 1] + f(i, ind - 1) + f(ind + 1, j)
            mini = min(mini, ans)
        
        dp[i][j] = mini
        return mini

    return f(1, c)

if __name__ == "__main__":
    cuts =  [3, 5, 1, 4]
    c = len(cuts)
    n = 7

    print("The minimum cost incurred:", min_cost(n, c, cuts))



# mem one shift right  
print()

def f( i, j, dp, s1, s2):
    # if i < 0 or j < 0:
    if i == 0 or j == 0:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
       
    # if s1[i] == s2[j]:
    if s1[i-1] == s2[j-1]:
        dp[i][j] = 1 + f( i - 1, j - 1, dp, s1, s2)
        return dp[i][j]

    dp[i][j] = max(f( i, j - 1, dp, s1, s2), f( i - 1, j, dp, s1, s2))
    return dp[i][j]

if __name__ == '__main__':

    s1 = "acd"
    s2 = "ced"
    n = len(s1) 
    m = len(s2) 
    # dp = [[-1]* m  for _ in range(n)]
    dp = [[-1]* (m+1)  for _ in range(n+1)]

    # print( f( n - 1, m - 1, dp, s1, s2))
    print( f( n  , m  , dp, s1, s2))



# MEMO  

# memoiza   aslo rep 

def f( i, j, dp, s1, s2):
    # Base case: If either of the strings has reached the end
    if i < 0 or j < 0:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
       
    if s1[i] == s2[j]:
        dp[i][j] = 1 + f( i - 1, j - 1, dp, s1, s2)
        return dp[i][j]

    dp[i][j] = max(f( i, j - 1, dp, s1, s2), f( i - 1, j, dp, s1, s2))
    return dp[i][j]
    
if __name__ == '__main__':

    s1 = "acd"
    s2 = "ced"
    n = len(s1)
    m = len(s2)
    dp = [[-1]* m  for _ in range(n)]
    print( f( n - 1, m - 1, dp, s1, s2))



# memeo also rep 

def lcsUtil(s1, s2, ind1, ind2, dp):
    if ind1 < 0 or ind2 < 0:
        return 0
    if dp[ind1][ind2] != -1:
        return dp[ind1][ind2]
    
    if s1[ind1] == s2[ind2]:
        dp[ind1][ind2] = 1 + lcsUtil(s1, s2, ind1 - 1, ind2 - 1, dp)
        return dp[ind1][ind2]

    dp[ind1][ind2] = max(lcsUtil(s1, s2, ind1, ind2 - 1, dp), lcsUtil(s1, s2, ind1 - 1, ind2, dp))
    return dp[ind1][ind2]
    

def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[-1 for j in range(m)] for i in range(n)]
#   dp = [[-1 ]*  m  for i in range(n)]
     
    return lcsUtil(s1, s2, n - 1, m - 1, dp)

def main():
    s1 = "acd"
    s2 = "ced"
    print("The Length of Longest Common Subsequence is", lcs(s1, s2))

if __name__ == '__main__':
    main()


# memoiza   as 

def lcsUtil(s1, s2, ind1, ind2, dp):
    # Base case: If either of the strings has reached the end
    if ind1 < 0 or ind2 < 0:
        return 0
    
    if dp[ind1][ind2] != -1:
        return dp[ind1][ind2]
       
    if s1[ind1] == s2[ind2]:
        dp[ind1][ind2] = 1 + lcsUtil(s1, s2, ind1 - 1, ind2 - 1, dp)
    else:
        dp[ind1][ind2] = max(lcsUtil(s1, s2, ind1, ind2 - 1, dp), lcsUtil(s1, s2, ind1 - 1, ind2, dp))
    
    return dp[ind1][ind2]

def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[-1 for j in range(m)] for i in range(n)]
    return lcsUtil(s1, s2, n - 1, m - 1, dp)

def main():
    s1 = "acd"
    s2 = "ced"
    print("The Length of Longest Common Subsequence is", lcs(s1, s2))

if __name__ == '__main__':
    main()
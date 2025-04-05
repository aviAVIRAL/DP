


Df= [-1]*4
print(Df)

# recursion 

def f(n):
    if n <= 1:
        return n
 
    sol = f(n-1) + f(n-2)
    return sol

if __name__ == "__main__":
    n = 5
    print(f(n))

# memoization 

def f(n, dp):
    if n <= 1:
        return n
 
    if dp[n] != -1:
        return dp[n]
    dp[n] = f(n-1, dp) + f(n-2, dp)
    return dp[n]

if __name__ == "__main__":
    n = 5
    dp = [-1] * (n+1)
    print(f(n, dp))

# alsro rep  Memoizaqtgion 

def f(n):
    if n <= 1:
        return n
 
    if dp[n] != -1:
        return dp[n]
    dp[n] = f(n-1) + f(n-2)
    print(dp)
    return dp[n]
if __name__ == "__main__":
    n = 5
    dp = [-1] * (n+1)

    print(f(n))


# tabuilar 

def main():
    n = 5
    dp = [-1]*(n+1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    print(dp[n])

if __name__ == "__main__":
    main()











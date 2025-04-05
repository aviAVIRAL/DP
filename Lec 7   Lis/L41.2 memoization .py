# striver rep  
def f(arr, n, ind, PrevIndx, dp):
    if ind == n:
        return 0
    
    if dp[ind][PrevIndx + 1] != -1:
        return dp[ind][PrevIndx + 1]

    len = f(arr, n, ind + 1, PrevIndx, dp)  # not take 

    if PrevIndx == -1 or arr[ind] > arr[PrevIndx]:  # take 
        len = max(len, 1 + f(arr, n, ind + 1, ind, dp))
    
    dp[ind][PrevIndx + 1] = len
    return len

if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    n = len(arr)
    dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
    print(f(arr, n, 0, -1, dp))

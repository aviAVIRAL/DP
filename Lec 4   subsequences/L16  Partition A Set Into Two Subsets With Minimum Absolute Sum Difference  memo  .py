


# memo izatiion 


def f(ind, target, arr, dp):
    if target == 0:
        return True
    if ind == 0:
        return arr[0] == target

    if dp[ind][target] != -1:
        return dp[ind][target]

    notTaken = f(ind - 1, target, arr, dp)
    taken = False
    if arr[ind] <= target:
        taken = f(ind - 1, target - arr[ind], arr, dp)

    dp[ind][target] = notTaken or taken

    return dp[ind][target]

def minSubsetSumDifference(arr):
    n = len(arr)
    totSum = sum(arr)
    # dp = [[-1 for i in range(totSum + 1)] for j in range(n)]
    dp = [[-1 ]*(totSum + 1) for _ in range(n)]

    for k in range(0, totSum + 1):
        f(n - 1, k , arr, dp)

    mini = int(1e9)
    for i in range(totSum + 1):
        if dp[n - 1][i] == True:
            diff = abs(i - (totSum - i))
            mini = min(mini, diff)
    return mini

def main():
    arr = [1, 2, 3, 4]
    print("The minimum absolute difference is:", minSubsetSumDifference(arr))

if __name__ == "__main__":
    main()






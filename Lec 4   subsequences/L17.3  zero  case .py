
# memoiza 

def countSubsets(ind, target, num, dp):

    # if target == 0:
    #     return 1

    # if ind == 0:                         
    #     return ( num[0] == target )

    if ind == 0:
        if target == 0 and num[0] == 0:  return 2  # Two ways: empty subset `{}` and `{0}`
        if target == 0 or num[0] == target:  return 1
        return 0



    if dp[ind][target] != -1:
        return dp[ind][target]

    notTaken = countSubsets(ind - 1, target, num, dp)

    taken = 0
    if num[ind] <= target:
        taken = countSubsets(ind - 1, target - num[ind], num, dp)

    dp[ind][target] = notTaken + taken
    return dp[ind][target]

def findWays(num, k):
    n = len(num)
    dp = [[-1] * (k + 1) for _ in range(n)]
    return countSubsets(n - 1, k, num, dp)

def main():
    arr = [0,0, 1]
    k = 1
    
    print("total number of subsets ", findWays(arr, k))

if __name__ == "__main__":
    main()





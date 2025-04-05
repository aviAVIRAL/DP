

# memoiza 

def countSubsets(ind, target, num, dp):
    # Base case: If the target sum is 0, there's exactly 1 way (empty subset)
    if target == 0:
        return 1

    if ind == 0:                         
        return ( num[0] == target )

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
    arr = [1, 2, 2, 3]
    k = 3
    
    print("The number of subsets found are", findWays(arr, k))

if __name__ == "__main__":
    main()


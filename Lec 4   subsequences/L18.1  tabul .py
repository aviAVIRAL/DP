

mod=int(1e9+7)
def findWays(num, tar):
    n = len(num)
    dp = [[0] * (tar + 1) for _ in range(n)]
    
    if num[0] == 0:
        dp[0][0] = 2 # 2 cases - pick and not pick
    else:
        dp[0][0] = 1 # 1 case - not pick
    
    if num[0] != 0 and num[0] <= tar:
        dp[0][num[0]] = 1 # 1 case - pick
    
    for ind in range(1, n):
        for target in range(tar + 1):
            notTaken = dp[ind - 1][target]
            taken = 0
            if num[ind] <= target:
                taken = dp[ind - 1][target - num[ind]]
        
            dp[ind][target] = (notTaken + taken) % mod
    return dp[n - 1][tar]

def countPartitions(n, d, arr):
    totSum = sum(arr)
    
    # Checking for edge cases
    if (totSum - d) < 0 or (totSum - d) % 2:
        return 0
    
    return findWays(arr, (totSum - d) // 2)

def main():
  arr = [5, 2, 6, 4]
  n = len(arr)
  d = 3
  print("The number of subsets found are", countPartitions(n, d, arr))
if __name__ == "__main__":
  main()

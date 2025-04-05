

# memization convert into memo  help in L16 concept 

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
        taken = f(ind - 1, target - arr[ind],arr,dp)

    dp[ind][target] = (notTaken or taken)

    print()
    print(dp)
    print()

    return dp[ind][target]


if __name__ == "__main__":

    arr = [1, 2, 3, 4]
    n = len(arr)
    k = 4
    dp = [[-1 for j in range(k + 1)] for i in range(n)]
    
    for i in range(0, k+1 ):
        ans = (f(n-1, i, arr, dp))
        print(ans)



# final op  
# [[-1,  -1  ,   -1,    -1, -1], 
#  [-1, True, True, True, False],
#  [-1, True, True, True, True], 
#  [-1, True, True, True, True]]




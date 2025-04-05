

# memization 

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

    return dp[ind][target]

def subsetSumToK(n, k, arr):
    dp = [[-1 for j in range(k + 1)] for i in range(n)]

    return f(n - 1, k, arr, dp)

def main():
    arr = [1, 2, 3, 4]
    k = 4
    n = len(arr)

    if subsetSumToK(n, k, arr):
        print("Subset with the given target found")
    else:
        print("Subset with the given target not found")

if __name__ == "__main__":
    main()


# # op 
# [[-1, -1, -1, -1, -1], 
#  [-1, True, -1, -1, False], 
#  [-1, -1, -1, -1, True],
#  [-1, -1, -1, -1, True]]

# .........................................................................

# ASLO REP RE 
# BUS PICK NOT PICK UPPER NICHE KR DITYA HAI   
# memization 

def f(ind, target, arr, dp):
    if target == 0:
        return True

    if ind == 0:
        return arr[0] == target

    if dp[ind][target] != -1:
        return dp[ind][target]
   
    taken = False
    if arr[ind] <= target:
        taken = f(ind - 1, target - arr[ind],arr,dp)

    notTaken = f(ind - 1, target, arr, dp)
    
    dp[ind][target] = (notTaken or taken)

    return dp[ind][target]

def subsetSumToK(n, k, arr):
    dp = [[-1 for j in range(k + 1)] for i in range(n)]

    return f(n - 1, k, arr, dp)

def main():
    arr = [1, 2, 3, 4]
    k = 4
    n = len(arr)

    if subsetSumToK(n, k, arr):
        print()
        print("true")
    else:
        print()
        print("False")

if __name__ == "__main__":
    main()


# # op 
# [[-1, -1, -1, -1, -1], 
#  [-1, True, -1, -1, False], 
#  [-1, -1, -1, -1, True],
#  [-1, -1, -1, -1, True]]

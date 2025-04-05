
# Burst Balloons|(DP-51)  

# recurssion   

def f(i, j, arr):
    if i > j:
        return 0

    maxi = float('-inf')

    for ind in range(i, j + 1):
        cost = arr[i - 1] * arr[ind] * arr[j + 1] + f(i, ind - 1, arr) + f(ind + 1, j, arr)
        maxi = max(maxi, cost)

    return maxi

def maxCoins(arr):
    n = len(arr)

    arr.insert(0, 1)  
    arr.append(1)
    
#  arr = [1] + arr + [1]         also rep  

    return f(1, n, arr)

if __name__ == "__main__":
    a = [3, 1, 5, 8]
    ans = maxCoins(a)
    print(ans)


print()
print()

# Burst Balloons|(DP-51)  

# recurssion   

def ff(i, j, arr):
    if i > j:
        return 0

    maxi = float('-inf')

    for ind in range(i, j + 1):
        cost = arr[i - 1] * arr[ind] * arr[j + 1] + f(i, ind - 1, arr) + f(ind + 1, j, arr)
        maxi = max(maxi, cost)

    return maxi

def maxCoins(arr):
    n = len(arr)
    # arr.insert(0, 1)
    # arr.append(1)
   
    # arr.append(1)
    return ff(1, n, arr)

if __name__ == "__main__":
    a = [3, 1, 5, 8]
    ans = maxCoins(a)
    print(ans)



print()


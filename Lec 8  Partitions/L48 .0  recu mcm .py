# DP 48. Matrix Chain Multiplication | MCM 

# recursion   

def f(arr, i, j):
    # Base condition
    if i == j:
        return 0

    mini = int(1e7)     

    # Partitioning loop
    for k in range(i, j):
        ans = f(arr, i, k) + f(arr, k + 1, j) + arr[i - 1] * arr[k] * arr[j]
        mini = min(mini, ans)

    return mini

def matrixMultiplication(arr, N):
    i = 1
    j = N - 1
    return f(arr, i, j)

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    n = len(arr)
    print("The minimum number of operations is", matrixMultiplication(arr, n))


print()
# recursion   aslo    repre    nested  function 

def matrixMultiplication(arr, N):
    i = 1
    j = N - 1
# ----------------------------------------
    def f( i, j):
        # Base condition
        if i == j:
            return 0
        
        mini = int(1e7)    

        # Partitioning loop
        for k in range(i, j):
            ans = f( i, k) + f( k + 1, j) + arr[i - 1] * arr[k] * arr[j]
            mini = min(mini, ans)

        return mini
# ----------------------------------------

    return f( i, j)

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    n = len(arr)
    print("The minimum number of operations is", matrixMultiplication(arr, n))

print()

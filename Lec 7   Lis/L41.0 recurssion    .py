

#      Longest Increasing Subsequence        | (DP-41



# recuression  frame work   

def f(arr, n,     ind, PrevIndx):
   
    if ind == n:
        return 0

    NotTake = 0 + f(arr, n,     ind + 1, PrevIndx)

    take = 0

    if PrevIndx == -1 or arr[ind] > arr[PrevIndx]:
        take = 1 + f(arr, n,     ind + 1, ind)

    return max(NotTake, take)

if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    n = len(arr)

    print( f(arr, n,     0, -1) )

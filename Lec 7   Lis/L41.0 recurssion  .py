

# striver rep 

# recuression   struver   

def f(arr, n,     ind, PrevIndx):
   
    if ind == n:
        return 0

    len = 0 + f(arr, n,     ind + 1, PrevIndx) #  not take 

    if PrevIndx == -1 or arr[ind] > arr[PrevIndx]:  # take 
        len =  max(len, 1 + f(arr, n,     ind + 1, ind) )

    return len

if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    n = len(arr)

    print( f(arr, n,     0, -1) )

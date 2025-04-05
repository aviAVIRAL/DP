


print()
print()


# recurrences 

def f(ind):
    if ind == 0:
        return 0

    jumpOne = f(ind - 1) + abs(arr[ind] - arr[ind - 1])

    jumpTwo = float('inf')  
    # 
    if ind >=2 :
        jumpTwo = f(ind - 2) + abs(arr[ind] - arr[ind - 2])

    return min(jumpOne, jumpTwo)

if __name__ == "__main__":
    arr = [30, 10, 60, 10, 60, 50]
    n = len(arr)
    print(f(n - 1))
print()
print()
print()


# DP 42. Printing Longest Increasing Subsequence 



def f(arr):
    n = len(arr)
    dp = [1] * n  # DP array initialized to 1
    Hash = list(range(n))  # To track the previous index for LIS reconstruction
    maxi = 1  # Stores the maximum LIS length
    last_index = 0  # To store the last index of LIS

    for i in range(n):
        for prev in range(i):
            if arr[prev] < arr[i] and  1 + dp[prev] > dp[i]:  # Valid LIS condition
                dp[i] = 1 + dp[prev]  # Update DP value
                Hash[i] = prev  # Store previous index

        if dp[i] > maxi:  # Update max LIS length and last index
            maxi = dp[i]
            last_index = i

    # LIS Reconstruction
    Lis = [ ]
    Lis.append(arr[last_index])
    while Hash[last_index] != last_index:
        last_index = Hash[last_index]
        Lis.append(arr[last_index])
    Lis.reverse()  # Reverse to get correct order

    return maxi, Lis

if __name__ == "__main__":
    arr = [5, 4, 11, 1, 16, 8]
    length, sequence = f(arr)
    print("Length of LIS:", length)
    print("LIS Sequence:", sequence)

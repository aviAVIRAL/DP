# Longest Bitonic Subsequence | (DP-46)


def longest_bitonic_sequence(arr):
    n = len(arr)

    # Initialize two dynamic programming lists for increasing and decreasing subsequences
    dp1 = [1] * n
    dp2 = [1] * n

    # Calculate the length of the longest increasing subsequence
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp1[i] = max(dp1[i], 1 + dp1[j])

    # Reverse the direction of nested loops to calculate the length of the longest decreasing subsequence
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[i]:
                dp2[i] = max(dp2[i], 1 + dp2[j]) 
 
    maxi = -1

    # Find the maximum length of bitonic subsequence by combining increasing and decreasing lengths
    for i in range(n):
        maxi = max(maxi, dp1[i] + dp2[i] - 1)

    return maxi


if __name__ == "__main__":
    arr = [1, 11, 2, 10, 4, 5, 2, 1]
    n = len(arr)

    print(" length of longest bitonic subsequence", longest_bitonic_sequence(arr))




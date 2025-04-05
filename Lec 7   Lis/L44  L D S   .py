

# Longest Divisible Subset | (DP-44)

def longest_divisible_subset(arr):
    n = len(arr)

    # Sort the array in ascending order
    arr.sort()

    # Initialize dp and hash arrays with 1s
    dp = [1] * n
    hash_arr = list(range(n))

    # Iterate through the array
    for i in range(n):
        for prev_index in range(i):
            if arr[i] % arr[prev_index] == 0 and 1 + dp[prev_index] > dp[i]:
                dp[i] = 1 + dp[prev_index]
                hash_arr[i] = prev_index

    ans = -1
    last_index = -1

    # Find the maximum length and its corresponding index
    for i in range(n):
        if dp[i] > ans:
            ans = dp[i]
            last_index = i

    # Reconstruct the divisible subset
    result = [arr[last_index]]

    while hash_arr[last_index] != last_index:
        last_index = hash_arr[last_index]
        result.append(arr[last_index])

    return result


if __name__ == "__main__":
    arr = [1, 16, 7, 8, 4]

    ans = longest_divisible_subset(arr)

    print("The longest divisible subset elements are:", ans)
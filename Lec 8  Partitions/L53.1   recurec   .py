
# Palindrome Partitioning - II | Front Partition : DP 53


# also rep re as  


def is_palindrome(temp):
    revtemp = temp[::-1]
    return( revtemp == temp)

def f(i, n, s):
    if i == n:
        return 0

    mini = float('inf')
    
    temp = ""
    # Iterate over possible substrings starting from index i
    for j in range(i, n):
        temp += s[j]
        if is_palindrome(temp):
             # If s[i...j] is a palindrome, calculate the cost
            cost = 1 + f(j + 1, n, s) 
            mini = min(mini, cost)

    return mini

def palindrome_partitioning(s):
    # Main function to find the minimum number of partitions
    n = len(s)
    return f(0, n, s) - 1  # Subtract 1 to exclude the initial unpartitioned string

if __name__ == "__main__":
    str = "BABABCBADCEDE"
    partitions = palindrome_partitioning(str)
    print("The minimum number of partitions:", partitions)


print()


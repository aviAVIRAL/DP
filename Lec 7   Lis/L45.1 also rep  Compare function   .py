# aslo repre  compareision function us ein l 


print()
print()

def f(s1, s2):
    n =  len(s1) 
    m =  len(s2) 

    if n != m + 1:
        return False

    i = 0
    j = 0

    while i < n:
        if j < m and s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            i += 1

    return i == n and j == m


s1 = "bcda"
s2 = "bcd"
print(f(s1, s2))


print()
print()
print()

def ff(s1, s2):
    n = len(s1)
    m = len(s2)

    if n != m + 1:
        return False

    i = 0  # Pointer for s1
    j = 0  # Pointer for s2

    while i < n and j < m:
        if s1[i] == s2[j]:
            j += 1  # Move pointer in s2
        i += 1  # Always move pointer in s1

    return j == m  # s2 should be fully matched


# Test Cases
s1 = "bcda"
s2 = "bcd"
print(ff(s1, s2))  # Expected output: True

s1 = "abcd"
s2 = "acd"
print(ff(s1, s2))  # Expected output: True

s1 = "abcdef"
s2 = "abc"
print(ff(s1, s2))  # Expected output: False (more than one character missing)
print()
print()
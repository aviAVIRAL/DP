

# Recursive

def f(s1, s2, i, j):
    if j < 0:
        return 1
    if i < 0:
        return 0
    
    if s1[i] == s2[j]:
        return f(s1, s2, i - 1, j - 1) + f(s1, s2, i - 1, j)
    else:
        return  f(s1, s2, i - 1, j)

s1 = "babgbag"
s2 = "bag"

print(f(s1, s2, len(s1) -1, len(s2)-1))

   


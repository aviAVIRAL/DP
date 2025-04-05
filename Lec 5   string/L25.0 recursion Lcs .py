
# RECU

def f( i, j, s1, s2):

    if i < 0 or j < 0:
        return 0
    
    if s1[i] == s2[j]:
        return  1 + f( i - 1, j - 1, s1, s2 )

    return max( f( i - 1, j, s1, s2), f( i, j - 1, s1, s2))


if __name__ == '__main__':
    s1 = "acd"
    s2 = "ced"
    n = len(s1)
    m = len(s2)
    print( f( n - 1, m - 1, s1, s2 ))



# recursion rep 1     

def f( ind1, ind2, s1, s2):

    if ind1 < 0 or ind2 < 0:
        return 0
    
    if s1[ind1] == s2[ind2]:
        return  1 + f( ind1 - 1, ind2 - 1, s1, s2 )

    return max( f( ind1 - 1, ind2, s1, s2), f( ind1, ind2 - 1, s1, s2))
    

def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    return f( n - 1, m - 1, s1, s2 )

def main():
    s1 = "acd"
    s2 = "ced"
    print("LCS  ", lcs(s1, s2))

if __name__ == '__main__':
    main()

print()

# aslo rep re 2 

def f( ind1, ind2, s1, s2):

    if ind1 < 0 or ind2 < 0:
        return 0
    
    if s1[ind1] == s2[ind2]:
        return  1 + f( ind1 - 1, ind2 - 1, s1, s2 )
    else : 
        return max( f( ind1 - 1, ind2, s1, s2), f( ind1, ind2 - 1, s1, s2))
    

def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    return f( n - 1, m - 1, s1, s2 )

def main():
    s1 = "acd"
    s2 = "ced"
    print("LCS  ", lcs(s1, s2))

if __name__ == '__main__':
    main()


print()
# repr  3 also rep    


def f( ind1, ind2, s1, s2):

    if ind1 < 0 or ind2 < 0:
        return 0
    
    if s1[ind1] == s2[ind2]:
        ans =   1 + f( ind1 - 1, ind2 - 1, s1, s2 )
    else : 
        ans =  max( f( ind1 - 1, ind2, s1, s2), f( ind1, ind2 - 1, s1, s2))
    return ans 

def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    return f( n - 1, m - 1, s1, s2 )

def main():
    s1 = "acd"
    s2 = "ced"
    print("LCS  ", lcs(s1, s2))

if __name__ == '__main__':
    main()


print()
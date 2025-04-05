

# recursion also rep 

# Evaluate Boolean arrression to True | Partition 

# Recursion

def evaluatearr(arr):
    n = len(arr)
    
    def f(i, j, isTrue):
        # Base case 1:
        if i > j:
            return 0
        # Base case 2:
        if i == j:
            if isTrue == 1:
                return int(arr[i] == 'T')
            else:
                return int(arr[i] == 'F')
        
        ways = 0
        for ind in range(i + 1, j, 2):
            lT = f(i, ind - 1, 1)
            lF = f(i, ind - 1, 0)
            rT = f(ind + 1, j, 1)
            rF = f(ind + 1, j, 0)

            if arr[ind] == '&':
                if isTrue:
                    ways += lT * rT
                else:
                    ways += lF * rT + lT * rF + lF * rF
            elif arr[ind] == '|':
                if isTrue:
                    ways += lF * rT + lT * rF + lT * rT
                else:
                    ways += lF * rF
            else:
                if isTrue:
                    ways += lF * rT + lT * rF
                else:
                    ways += lF * rF + lT * rT
        
        return ways
    
    return f(0, n - 1, 1)

if __name__ == "__main__":
    arr = "F|T^F"
    ways = evaluatearr(arr)
    print("The total number of ways:", ways)

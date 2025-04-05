#  memeo

def f(day, last, arr, dp):
    # Check if the result for this day and last points is already computed.
    if dp[day][last] != -1:
        return dp[day][last]

    # Base case: When we reach day 0, return the maximum point for the last day.
    if day == 0:
        maxi = 0
        for i in range(3):
            if i != last:
                maxi = max(maxi, arr[0][i])
        dp[day][last] = maxi
        return dp[day][last]

    maxi = 0
    # Iterate through all activities for the current day.
    for i in range(3):
        if i != last:
            # Calculate the total arr for the current day's points and recursively call for the previous day.
            points = arr[day][i] + f(day - 1, i, arr, dp)
            maxi = max(maxi, points)

    # Store the maximum arr in the DP table and return it.
    dp[day][last] = maxi

    return dp[day][last]


def ninjaTraining(n, arr):
    # Initialize a DP table to store the computed results.
    dp = [[-1 for j in range(n+1)] for i in range(n)]
    # dp = [[-1]*(n+1) for i in range(n)] #  also pre 
    # dp = [[-1 for j in range(4)] for i in range(n)] also rep 
    # Start the recursive function from the last day with no previous points.
    return f(n - 1, 3, arr, dp)

def main():
    # Define the arr matrix for each day.
    arr = [[10, 40, 70],
              [20, 50, 80],
              [30, 60, 90]]

    n = len(arr)  # Get the number of days.
    # Call the ninjaTraining function to find the maximum arr.
    print(ninjaTraining(n, arr))

if __name__ == '__main__':
    main()

# memo i zation  
# also rep  as 
    # dp[day][last] = 0  
    # for i in range(3):
    #     if i != last:
    #         points = arr[day][i] + f(day - 1, i, arr, dp)
    #         dp[day][last] = max(dp[day][last], points)

    # return dp[day][last]

def f(day, last, arr, dp):
    if dp[day][last] != -1:
        return dp[day][last]
    if day == 0:
        maxi = 0
        for i in range(3):
            if i != last:
                maxi = max(maxi, arr[0][i])
        dp[day][last] = maxi
        return dp[day][last]
# importsanst     
    dp[day][last] = 0  
    for i in range(3):
        if i != last:
            points = arr[day][i] + f(day - 1, i, arr, dp)
            dp[day][last] = max(dp[day][last], points)

    return dp[day][last]

def ninjaTraining(n, arr):
    dp = [[-1 for j in range(n+1)] for i in range(n)]
    return f(n - 1, 3, arr, dp)

def main():
    arr = [[10, 40, 70],
              [20, 50, 80],
              [30, 60, 90]]

    n = len(arr)  # Get the number of days.
    print(ninjaTraining(n, arr))

if __name__ == '__main__':
    main()

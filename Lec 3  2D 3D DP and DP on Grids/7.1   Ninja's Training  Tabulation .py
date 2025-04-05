

# tabulation 

def ninjaTraining(n, arr):
    # Initialize a DP table with dimensions (n x 4) to store the maximum arr.
    dp = [[0 for j in range(4)] for i in range(n)]

    # Initialize the DP table for day 0 with base cases.
    dp[0][0] = max(arr[0][1], arr[0][2])
    dp[0][1] = max(arr[0][0], arr[0][2])
    dp[0][2] = max(arr[0][0], arr[0][1])
    dp[0][3] = max(arr[0][0], max(arr[0][1], arr[0][2]))

    # Loop through the days starting from the second day.
    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0  # Initialize the maximum arr for the current day and last points.
            for i in range(3):
                if i != last:
                    # Calculate the total arr for the current day's points and the previous day's maximum arr.
                    points = arr[day][i] + dp[day - 1][i]
                    dp[day][last] = max(dp[day][last], points)

    # # also repr .
    # for day in range(1, n):
    #     for last in range(4):
    #         maxi = 0  # Use maxi to track the maximum arr for this day and last points.
    #         for i in range(3):
    #             if i != last:
    #                 # Calculate the total arr for the current day's points.
    #                 points = arr[day][i] + dp[day - 1][i]
    #                 maxi = max(maxi, points)  # Update maxi with the maximum value.
    #         dp[day][last] = maxi  # Store the maximum value in the DP table.


    # Return the maximum arr achievable after the last day with any points.
    # print(dp)
    return dp[n - 1][3]

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

# also repre as  
def ninjaTraining(n, arr):
    # Initialize a DP table with dimensions (n x 4) to store the maximum arr.
    dp = [[0 for _ in range(4)] for _ in range(n)]

    # Initialize the DP table for day 0 with base cases.
    dp[0][0] = max(arr[0][1], arr[0][2])
    dp[0][1] = max(arr[0][0], arr[0][2])
    dp[0][2] = max(arr[0][0], arr[0][1])
    dp[0][3] = max(arr[0][0], max(arr[0][1], arr[0][2]))

    # Loop through the days starting from the second day.
    for day in range(1, n):
        for last in range(4):
            maxi = 0  # Use maxi to track the maximum arr for this day and last points.
            for i in range(3):
                if i != last:
                    # Calculate the total arr for the current day's points.
                    points = arr[day][i] + dp[day - 1][i]
                    maxi = max(maxi, points)  # Update maxi with the maximum value.
            dp[day][last] = maxi  # Store the maximum value in the DP table.

    # Return the maximum arr on the last day with no restriction on the last points.
    return dp[n - 1][3]

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

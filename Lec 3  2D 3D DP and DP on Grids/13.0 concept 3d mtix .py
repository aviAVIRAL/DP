

matrix = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
n = len(matrix)
m = len(matrix[0])

# Initialize a memoization table with -1 values
dp = [[[-1 for j in range(m)] for i in range(m)] for k in range(n)]
print(dp)
print()


# ...... op ....

dp = [
  [  # For row 0
    [-1, -1, -1, -1],  # First person at column 0, Second person at column 0, 1, 2, 3
    [-1, -1, -1, -1],  # First person at column 1, Second person at column 0, 1, 2, 3
    [-1, -1, -1, -1],  # First person at column 2, Second person at column 0, 1, 2, 3
    [-1, -1, -1, -1],  # First person at column 3, Second person at column 0, 1, 2, 3
  ],
  [  # For row 1
    [-1, -1, -1, -1],  # First person at column 0, Second person at column 0, 1, 2, 3
    [-1, -1, -1, -1],  # First person at column 1, Second person at column 0, 1, 2, 3
    [-1, -1, -1, -1],  # First person at column 2, Second person at column 0, 1, 2, 3
    [-1, -1, -1, -1],  # First person at column 3, Second person at column 0, 1, 2, 3
  ],
  [  # For row 2
    [-1, -1, -1, -1],  # First person at column 0, Second person at column 0, 1, 2, 3
    [-1, -1, -1, -1],  # First person at column 1, Second person at column 0, 1, 2, 3
    [-1, -1, -1, -1],  # First person at column 2, Second person at column 0, 1, 2, 3
    [-1, -1, -1, -1],  # First person at column 3, Second person at column 0, 1, 2, 3
  ]
]

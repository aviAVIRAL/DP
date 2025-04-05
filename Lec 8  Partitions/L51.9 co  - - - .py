

# recursion also rep 

# Evaluate Boolean arrression to True | Partition 

# # Recursion
#         if i == j:
#             if isTrue == 1:
#                 return int(arr[i] == 'T')
#             else:
#                 return int(arr[i] == 'F')

# if __name__ == "__main__":
#     arr = "F|T^F"
#     ways = evaluatearr(arr)
#     print("The total number of ways:", ways)





print()

def f(arr):
    if len(arr) > 1 : 
        return arr[2] == 2

arr = [0 , 1, 2, 3, 4 ]

sol = f(arr)
print(sol)

print()
def f(arr):
    if len(arr) > 1 : 
        return arr[2] == 3

arr = [0 , 1, 2, 3, 4 ]

sol = f(arr)
print(sol)


print()
def f(arr):
    if len(arr) > 1 : 
        return int(arr[2] == 2)

arr = [0 , 1, 2, 3, 4 ]
sol = f(arr)
print(sol)

print()

def f(arr):
    if len(arr) > 1 : 
        return int(arr[2] == 3)

arr = [0 , 1, 2, 3, 4 ]
sol = f(arr)
print(sol)

print()
# print()
# print()
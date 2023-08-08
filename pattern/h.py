# n = int(input("enter a no"))
# for i in range(n,1,-1):
#   for j in range(i):
#     print(j,end="")
#     j-=1
#   print()

n = int(input("enter the number of rows:"))
for row in range(n,0,-1):
  for col in range(1,row+1):
    print(col,end="")
  print()

# optimize the code in order of O(n)
n = int(input("enter the number of rows:"))

for row in range(n, 0, -1):
    row_sum = (row * (row + 1)) // 2  # Calculate sum of numbers in the row
    print(" ".join(str(num) for num in range(1, row_sum + 1)))

# 1 2 3 4 5 6
# 1 2 3
# 1

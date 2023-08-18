""" print in wave form 
ex:-  1 2 3
      4 5 6
      7 8 9
output:- 
      1 4 7 8 5 2 3 6 9
  
explation: 
   when its even column we are moving down else its odd column we are moving Up.....

"""

str = input().strip().split(" ")
n = int(str[0])
m = int(str[1])
l = [int(i) for i in input().strip().split(" ")]

out = [[l[i*m+j] for j in range(m)] for i in range(n)]

print(out)

n = len(out)
m = len(out[0])

for j in range(m):
  if j%2==0:
    for i in range(n):
      print(out[i][j], end=" ")
  else:
    # i = n-1
    # while(i>=0):
    #   print(out[i][j], end=" ")
    #   i=i-1
    #we can also use For loop rather than while loop

    for i in range(n-1,-1,-1):
      print(out[i][j],end=" ")


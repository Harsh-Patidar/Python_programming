#  * * * * *
#  * * * *
#  * * *
#  * *
#  *

num = int(input("enter the no"))
for i in range(num,0,-1):
  print(" *"*i) 

#------------------------------------

n = int(input("enter the no"))
for i in range(n,0,-1):
  for j in range(0,i):
    print("*",end="")
  print()

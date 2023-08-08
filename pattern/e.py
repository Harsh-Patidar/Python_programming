
#   *** 
#  *   *
#  *   *
#  *****
#  *   *
#  *   *
#  *   *

for row in range(7):
  for col in range(5):
    if ((col==0 or col == 4 )and row!=0)  or ((row==0 or row==3) and (col >0 and col<4)):
      print("*",end="")
    else:
      print(end=" ")

  print()

#--------------------------------------------------------------

n=1
for i in range(1,11):
  for j in range(i):
    print(n,end="")
  n=n+1
  print()

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
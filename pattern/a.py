#Q.1
# *
# **
# ***
# ****
def patter(x):
  for i in range(1,x+1):
    for j in range(1,i+1):
      print("*",end="")
    print()
patter(5)

#-------------#
#Q.2
# *
# ****
# *******
# **********
def patter_a(y):
  k = 1
  for i in range(1,y+1):
    for j in range(1,k+1):
      print("*",end="")
    k=k+3
    print()

patter_a(5)

#------------#
#Q.3
#chatgpt
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
def triangle(n):
  for i in range(1,n+1):
    print(" "*(n-i) + " *"*(i))
    
  
triangle(5)
#-------------------------
def patter_b(c):
  for i in range(0,c):
    for j in range(0,c-i-1):
      print(end=" ")
    for j in range(0,i+1):
      print("*",end=" ")
    print()
patter_b(10)
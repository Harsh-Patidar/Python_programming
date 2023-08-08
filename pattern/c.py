#     * * * * * * *
#      * * * * * *
#       * * * * *
#        * * * *
#         * * *
#          * *
#           *
#          * *
#         * * *
#        * * * *
#       * * * * *
#      * * * * * *
#     * * * * * * *

num = int(input("enter the no:"))
for i in range(num,1,-1):
  print(" "*(num-i)+" *"*i)
for j in range(1,num):
  print(" "*(num-j)+" *"*j)

#O(n)
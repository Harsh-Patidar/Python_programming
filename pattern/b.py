# enter the no:5
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *

num = int(input("enter the no:"))
for i in range(num,0,-1):
  print(" "*(num-i)+" *"*i)
#--------------------------------
# enter the no:10
#           *
#          * *
#         * * *
#        * * * *
#       * * * * *
#      * * * * * *
#     * * * * * * *
#    * * * * * * * *
#   * * * * * * * * *
num2=int(input("enter the no:"))
for j in range(1,num2+1):
  print(" "*(num2-j)+" *"*j)
  
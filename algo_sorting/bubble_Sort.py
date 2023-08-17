# Bubble Sort
#Some times referred as sinking sort,is a simple sorting algorithm which sorts n number of elements in the list by comparing the each pair of adjacent items and swaps them if they are in wrong order.


list1= [10,15,4,23,0]
for j in range(len(list1)-1):
  for i in range(len(list1)-1-j): # -j aagr use nhi krege har baar ek step extra use hogi
    if list1[i]>list1[i+1]:
      list1[i],list1[i+1] = list1[i+1],list1[i]
      print(list1)
    else:
      print(list1)
  print()

# Another method

list1= [10,15,4,23,0]
for j in range(len(list1)-1,0,-1):
  for i in range(j):
    if list1[i]>list1[i+1]:
      list1[i],list1[i+1] = list1[i+1],list1[i]
      print(list1)
    else:
      print(list1)
  print() 

# Another method

list1=[]
num = int(input("how many no you want to enter"))
print("enter values")
for k in range(num):
  list1.append(int(input()))

print("unsorted list",list1)

for j in range(len(list1)-1,0,-1):
  for i in range(j):
    if list1[i]>list1[i+1]:
      list1[i],list1[i+1] = list1[i+1],list1[i]
      print(list1)
    else:
      print(list1)
  print() 
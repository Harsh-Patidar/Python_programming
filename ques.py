#add krna hai harsh..bhai...smj jaana yr....bhul na jaaana
n, m = [int(i)  for i in input().split()]
a = [int(i) for i in input().split()]
max = 0
ans = 0
for i in range(n):
    x = a[i]//m
    if a[i] % m != 0:
        x += 1
    if x >= max:
        max = x
        ans = i+1
print(ans)

#by sir
n, m = [int(i)  for i in input().split()]
arr = [int(i) for i in input().split()]

def last_one(arr,n):
  p=0
  for i in arr:
    if i>0:
  return p==1
  


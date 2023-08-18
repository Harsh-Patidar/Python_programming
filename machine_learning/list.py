# # 2D ARRAY 

# l=[[1,2,3],[4,5,6]]
# print(l)
# print(l[0][1])

# l1=[[1,2,3] for i in range(10)]
# print(l1)

# l11= [[j for j in range(5)] for i in range(10)]
# print(l11)

# l12=[[5*i+j for j in range(5)]for i in range(10)]
# print(l12)

# how to take input in 2d array

str = input().strip().split(" ")
n = int(str[0])
m = int(str[1])

k=[ int(i)for i in input().strip().split(" ")]
out = []
for i in range(n):
  out.append([])
  for j in range(m):
    out[i].append(k[i*m+j])
print(out)
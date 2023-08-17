"""# list = [56,3,2,78,6,0]
list = [56,0,2,2,6,0]
for i in range(len(list)):
  list_min = min(list[i:])
  list_ind = list.index(list_min)
  list[i],list[list_ind]= list[list_ind],list[i]
print(list)

#above code is only applicable for non duplicate number

list = [56,0,2,2,6,0]

for i in range(len(list)-1): # yaha per len -1 isliye li hai...aap 6 bar iterate na kr ke sirf 5 baar kre.....kyo ki last vala element aapne aap sort ho kr aaye ga

  list_min = min(list[i:])
  list_ind = list.index(list_min,i)
  list[i],list[list_ind]= list[list_ind],list[i]
print(list)


# Now, without using min() method we have to find the sorted list.
"""
# list=[34,5,6,81,0,5]
# for i in range(len(list)-1):
#   for j in range(i+1,len(list)):
#     if list[j]<list[i]:
#       list[i],list[j]=list[j],list[i]
#       print(list)

list=[34,5,6,81,0,5]
for i in range(len(list)-1):
  m_val = list[i]
  for j in range(i+1,len(list)):
    if list[j]<m_val:
      m_val = list[j]
  m_ind = list.index(m_val,i)
  if list[i] != list[m_ind]:
    list[i],list[m_ind]=list[m_ind],list[i]
print(list)

#   DEEP_COPY AND SHALLOW_COPY

import copy 
l=[10,[20,30],[40,50]]

l1=copy.deepcopy(l)
l[1].pop()
l1[2].append(60)
l1[1].pop(0)
print(l1)
print(l)
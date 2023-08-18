#file handling concept
"""
f = open("krishna.txt",'x')
f.close()

"""

#or.....
with open("sample.txt",'a') as f: #instead of writing 'w' use 'a' it print it multipal times
  f.write("sample line \n")
  f.write("congratulation")

#similary by using 'r'
with open ("sample.txt",'r') as f:
  for l in f.readlines(): print(l,end="")


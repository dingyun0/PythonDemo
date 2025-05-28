l1=[x*x for x in range(20)]
print(l1)

l2=[m+n for m in 'ABC' for n in 'abc']
print(l2)

l3=[x*x for x in range(20) if x%2==0]
print(l3)

import os
print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.items():
  print(k+':'+v)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k+'='+v for k,v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

print([x for x in range(20) if x%2==0])
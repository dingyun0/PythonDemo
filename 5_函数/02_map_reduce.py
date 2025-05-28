def normalize(name):
  return name[0].upper()+name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2=list(map(normalize,L1))
print(L2)

from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':'.'}
def a(s):
  i=s.index('.')
  print(i)
  m=len(s[i+1:])
  print(m)
  s=s[0:i]+s[i+1:]
  print(s)
  # lambda 关键字用于定义一个匿名函数,:后面是表达式，前面是参数
  # map和reduce都素函数在第一个参数，要迭代的可迭代对象在第二个参数
  return reduce(lambda x,y:x*10+y,map(lambda x:DIGITS[x],s))/(10**m)
print(a('123.456'))

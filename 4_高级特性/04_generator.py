# 一边循环一边计算
L=[x for x in range(10)]
g=(x for x in L)
# print(g)
# print(next(g))
# print(next(g))
# for i in g:
  # print(i)

# yield返回一个生成器对象，return单纯返回一个值
def odd():
  print('1')
  yield 1
  print('2')
  yield 2
  print('3')
  yield 3
  return '666'


o=odd()
# print(next(o))
# print(next(o))
# print(next(o))
# print(next(o))

for n in odd():
  print(n)

# for循环拿不到生成器的值，要捕捉错误才行

# 杨辉三角
def three():
  s=[1]
  while True:
    yield s
    # s = [1] + [2] + [3] 的结果是一个列表 [1, 2, 3]
    s=[1]+[s[i]+s[i+1] for i in range(len(s)-1)]+[1]
n=0
result=[]
for t in three():
  print(t)
  n=n+1
  if n==10:
    break

# 其中，genrtator就是一个迭代器,其他都只是一个可迭代对象
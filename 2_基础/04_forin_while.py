sum1=0
sum2=0
list1=[1,2,3,4]
tuple1=(5,6,7,8)
for x in list1:
  sum1+=x
for y in tuple1:
  sum2+=y
print(sum1+sum2)

result=range(5)
print(result)
print(list(result))
print(tuple(result))

sum=0
n=99
while(n>0):
  sum=sum+n
  n=n-2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for x in L:
  print(f'hello,{L}')


index = 0
while index < len(L):
    name = L[index]
    print(f"Hello, {name}!")
    index += 1

for i in range(100):
  if(i>10):
    break
  print(i)
  i=i+1

n=0
while n<10:
  n=n+1
  if n%2==0:
    continue
  print(n)
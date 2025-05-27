def count():
  fs=[]
  # 1,2,3
  for i in range(1,4):
    def f():
      # 1,4,9
      return i*i
    fs.append(f)
    print(fs)
  return fs

f1,f2,f3=count()
# 返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# print(f1())
# print(f2())
# print(f3())

# 使用闭包，就是内层函数引用了外层函数的局部变量。如果只是读外层变量的值，我们会发现返回的闭包函数调用一切正常
# 使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量。
def a():
  num=0
  def count():
    nonlocal num
    num=num+1
    return num
  return count

b=a()
print(b(),b(),b())

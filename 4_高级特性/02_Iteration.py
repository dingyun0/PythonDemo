def find(L):
  if len(L)==0:
    return (None,None)
  elif len(L)==1:
    return (L[0],L[0])
  else:
    min1=L[0]
    max1=L[0]
    for index,value in enumerate(L):
      print(index,value)
      if value<min1:
        min1=value
      elif value>max1:
        max1=value
    return (min1,max1)

result=find([5,3,6,8,2,99])
print(result)
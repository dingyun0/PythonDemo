from io import StringIO
f=StringIO()
f.write('111')
f.write('hello,world')
print(f.getvalue())


from io import BytesIO
f=BytesIO()
f.write('111'.encode('utf-8'))
print(f.getvalue())
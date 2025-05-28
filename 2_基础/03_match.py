args=['gcc','hello.c','world.c']
match args:
  case ['gcc']:
    print('1')
  case ['gcc',file1,*files]:
    print('2')
  case ['clean']:
    print('clean')
  case _:
    print('invalid command')
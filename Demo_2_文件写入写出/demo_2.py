def write(message):
    try:
        with open('data.txt','a',encoding='utf-8')as file:
            file.write(message+'\n')
        print('文件写入成功')
    except IOError as e:
        print(f'文件写入失败:{e}')

def read():
    with open('data.txt','r',encoding='utf-8')as file:
        lines=file.readlines()
        return [line.strip() for line in lines]


def main():
    write('hello,world')
    write('wobuhao')
    print(read())
if __name__=='__main__':
    main()
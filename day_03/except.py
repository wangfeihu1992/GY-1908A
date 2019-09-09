def div(a,b):
    try:
        c=a/b
    except:
        print("除数不能为0")
        return
    return c
print(div(19,8))


def oper_file():
    try:
        #g=open("test.txt",'w')
        g = open("test", 'w')
       # g.read()
        g.close()
        g.write("wwwwww")
    except FileNotFoundError:
        print("文件不存在")
    except ValueError:
        print("文件已关闭")
oper_file()

user_name
create_time











































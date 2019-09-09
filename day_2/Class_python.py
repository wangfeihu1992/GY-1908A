class Class_Demo():
    def abc(self):
        print("我是a")
    def cba(self):
        print("可乐")
        self.abc()

if __name__ == '__main__':
    c = Class_Demo()
    c.abc()
    c.cba()

# dergakio   要求生成两个新的字符串  drai  和egko

a = 'dergakio '
print(a[::2])
print(a[1::2])

c = 'ashkfdjhgoie'
print(c[:5])
print(c[1:4:-1])

d = "金额,用例,断言"
print(d.split(","))
t="谁啊,咋地了,我啊"
print(t.split(","))
e = '   adfdfgdgsdf    '
print(e.rstrip())
y='asdjfdk"123455'
print(y.replace('"',"'"))

# GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1
a = "GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1"
print(a[:3])
class Class_Demo():
    def a(self):
        print("https")
    def b(self):
        print("www.fiddler2.com")
    def c(self):
        print("UpdateCheck.aspx")
    def d(self):
        print("isBeta=False")
    def e(self):
        print("HTTP/1.1")
if __name__ == '__main__':
    q = Class_Demo()
    q.a()
    q.b()
    q.c()
    q.d()
    q.e()

































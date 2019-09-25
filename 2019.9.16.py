#_author_='CX';
#date: 2019/9/16

# 面向对象程序编程练习
# 1．向 Square类中添加一个square_list类变量，要求每次新创建一个Square 对象时，新对象会被自动添加到列表中。
'''class Square():
    square_list=[]
    def __init__(self,w,l):
        self.width=w
        self.len=l
        self.square_list.append((self.width,self.len))
    def print_size(self):
        print("""{} by {}""".format(self.width,self.len))
s1=Square(12,15)
s2=Square(23,29)
s3=Square(34,39)
print(Square.square_list)
'''
# 2．修改 Square 类，要求在打印 Square 对象时，打印的信息为图形 4 个边的长 度。例如，假设创建一个Square(29)，则应打印29 by 29 by 29 by 29。
'''class Square():
    square_list=[]
    def __init__(self,l):
        self.len=l
        self.square_list.append((self.len,self.len,self.len,self.len))
    def print_size(self):
        print("""{} by {} by {} by {}""".format(self.len,self.len,self.len,self.len))
s1=Square(4)
print(s1.print_size())
'''

# 3．编写一个函数，接受两个对象作为参数，如果为相同的对象则返回True，反之 返回False。
'''def f(x,y):
    if x==y:
        return True
    else:
        return False
print(f(3,3))
'''

from flask import Flask
app=Flask(__name__) # 新建一个Flask可运行实体
@app.route('/') # 在运行实体上绑定URL路由
def index():
    return "hello,world!"
app.run(port='8000')

# 这是一个示例 Python 脚本。
# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
# coding=utf-8

import sys
import os


def strlearn():
    strs = "123456789";
    print(strs);


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


def testwhile():
    a = 1
    while a < 10:
        b = str(a)
        print("a" + b)
        a = a + 1


def testiter():
    a = [1, 2, 3, 4, 5, 9]
    it = iter(a)
    while True:
        try:
            n = next(it)
            if n:
                print(n)
        except StopIteration:
            break


def testforiter():
    a = [1, 2, 3, 4, 5]
    it = iter(a)
    for x in it:
        print(x)


def testselfitor():
    class testit:
        def __iter__(self):
            # 自我迭代
            self.a = 1
            return self

        def __next__(self):
            x = self.a
            self.a = self.a + 1
            if self.a > 20:
                raise StopIteration
            return x

    tt_class = testit()
    it = iter(tt_class)
    print(next(it), 1)
    print(next(it), 2)
    i = 1
    while i < 30:
        print(next(it), i)
        i = i + 1


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


def fib(n):
    a, b = 0, 1
    m = 0
    while m < n:
        a, b = b, a + b
        print(b, end=",")
        m += 1


def fib2(n):
    a, b = 0, 1
    m = 0
    result = []
    while m < n:
        a, b = b, a + b
        result.append(b)
        m += 1
    print(result)


def openfile():
    f = open("zhzabc.txt", "a+", encoding='utf-8')
    thecontent = f.read()
    print(thecontent)
    f.write(u"what the fuck 张宏镇啊 睿羿科技啊  山东兆物啊")
    f.close()


def readfile():
    f = open("zhzabc.txt", "r", encoding='utf-8')
    while True:
        culine = f.readline()
        print(culine)
        if culine == '':
            break;
def operfile():
    f=open("zhzabc.txt","r", encoding='utf-8')
    thefilename=f.name
    thefileno=f.fileno()
    thefileencoding=f.encoding
    thefilemode=f.mode
    isatty=f.isatty()
    print("thefilename=",thefilename,",thefileno=",thefileno,",thefileencoding=",thefileencoding,",thefilemode=",thefilemode,",isatty=",isatty)
    f.close()

def testos():
    res =os.access("zhzabc.txt",os.F_OK)
    print("是否存在?",res)
    res = os.access("zhzabc.txt", os.R_OK)
    print("是否可读?", res)
    res = os.access("zhzabc.txt", os.W_OK)
    print("是否可写?", res)
    res = os.access("zhzabc.txt", os.X_OK)
    print("是否可执行?", res)


def testos2dir():
    path=os.getcwd()
    print("当前工作目录getcwd()",path)
    print("当前工作目录getcwdb()", os.getcwdb())
    newpath="D:\\"
    os.chdir(newpath)
    print("当前工作目录", os.getcwd())
def testos2chflags():
    import stat
    path="zhzabc.txt"
    '''
    stat.UF_NODUMP: 非转储文件
    stat.UF_IMMUTABLE: 文件是只读的
    stat.UF_APPEND: 文件只能追加内容
    stat.UF_NOUNLINK: 文件不可删除
    stat.UF_OPAQUE: 目录不透明，需要通过联合堆栈查看
    stat.SF_ARCHIVED: 可存档文件(超级用户可设)
    stat.SF_IMMUTABLE: 文件是只读的(超级用户可设)
    stat.SF_APPEND: 文件只能追加内容(超级用户可设)
    stat.SF_NOUNLINK: 文件不可删除(超级用户可设)
    stat.SF_SNAPSHOT: 快照文件(超级用户可设)
    '''
    res=os.chflags(path, stat.UF_APPEND)
    print("文件模式设置成功",res)

def testclass():
    class student:
        thename="default"
        name=''
        age=15
        theweight=200
        _money=50
        __money=0
        def __init__(self,name,age,theweight):
            self.name=name
            self.age=age
            self.theweight=theweight
            print("构造函数开始构造")

        def name(self):
            return self.thename

        def tostringzhz(self):
            1==1
            print("_money",self._money)
            print("__money", self.__money)

    stu= student("zhz",15,10)
    #print("studentname:",stu.name());
    #stu.tostringzhz()
    print("_money",stu._money)
    #print("__money", stu.__money)
def testanotherclass():
    # 类定义
    class people:
        # 定义基本属性
        name = ''
        age = 0
        # 定义私有属性,私有属性在类外部无法直接进行访问
        __weight = 0

        # 定义构造方法
        def __init__(self, n, a, w):
            self.name = n
            self.age = a
            self.__weight = w

        def speak(self):
            print("%s 说: 我 %d 岁。" % (self.name, self.age))

    # 单继承示例
    class student(people):
        grade = ''

        def __init__(self, n, a, w, g):
            # 调用父类的构函
            people.__init__(self, n, a, w)
            self.grade = g

        # 覆写父类的方法
        def speak(self):
            print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))
    stu=student('zhz',15,20,3)
    stu.speak()
    super()


def zhz_sqrt():
    num=2**3;
    print("2的3次方:",num)
    num2=16**0.5
    print("16平方根",num2)

def zhz_random():
    import random
    print("random.random()",random.random())
    print("random.randint(1,100)", random.randint(1,100))
    print("random.randint(1,100)", random.randint(1, 100))
    print("random.randrange(1,100)", random.randrange(1, 100))


'''
30 个人在一条船上，超载，需要 15 人下船。
于是人们排成一队，排队的位置即为他们的编号。
报数，从 1 开始，数到 9 的人下船。
如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？
'''
#def yuesefu_live_death():

def testbinarysearch(arr,st,et,x):
    print("开始位置",st,"结束位置",et)
    #最后都没有找到
    if et>=0:
        mid=int((et-1)/2+1)
        print("mid 值",mid)
        if arr[mid]  == x:
            return mid
        elif arr[mid]>x:
            #从小范围去找
            #start=1
            stop=mid-1
            return   testbinarysearch(arr, st, stop, x)
        elif arr[mid]<x:
            #从大范围去找
            start=mid+1
            return testbinarysearch(arr, start, et, x)
    else:
        return -1













if __name__ == "__main__":

    arr=[1,2,3,4,5,6,7,8]
    index=testbinarysearch(arr,0,len(arr),1)
    print("找到的位置在:",index)

    #zhz_random()
    #zhz_sqrt()
    #testanotherclass()
    #testclass()
    #testos2dir()
    #testos2dir()
    #testos2dir
    #testos()
    #operfile()
    #readfile()
    #openfile()
    # fib2(5)
    # fib(5)
    # print(zhzadd.zhzadd(100, 200))
    # print(zhzadd.zhzadd(100, 200))

    # print(sys.path)
    # f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
    # while True:
    #     try:
    #         print(next(f))
    #     except StopIteration:
    #         sys.exit()
    #     finally:
    #         a1=1
    #  print(next(f))

    # testselfitor()

    # testforiter()
    # testiter()
    # testwhile()
    '''
        print_hi("zhz")
    '''

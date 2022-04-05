# 这是一个示例 Python 脚本。


# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
# coding=utf-8


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



if __name__ == "__main__":
    readfile()
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

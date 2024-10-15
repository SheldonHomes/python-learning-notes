"""
异常的传递性：当函数或方法中出现异常时，会将异常传递给调用该函数或方法的代码，直到被捕获为止

"""

def func1():
    print("func1 start")
    num = 1 / 0
    print("func1 end")

def func2():
    print("func2 start")
    func1()
    print("func2 end")

def main():
    print("main start")
    try:
        func2()
    except Exception as e:
        print("捕获到异常：", e)
    print("main end")

if __name__ == '__main__':
    main()
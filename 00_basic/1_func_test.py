

# 定义一个普通函数
def say_hello(name):
    return "Hello Python!, hello " + name


def normal_func():
    print('*' *50 ,'normal_func', '*'*50)

    # 1. 函数赋值给变量
    func_1 = say_hello  # 注意：这里没有加括号，只是赋值，不执行函数
    print(type(func_1))
    print(func_1('Bob'))  # 输出：Hello Python!（通过变量调用函数）


def exe_func(funcc, *args, **kwargs):
    print(f"准备执行函数 ：{funcc.__name__}")
    result = funcc(*args, **kwargs)
    return result

    # 定义待执行的函数


def add(a, b):
    return a + b

def func_param_test():
    print('*' *50 ,'func_param_test', '*'*50)
    # 2. 把add函数作为参数传给execute_func
    result = exe_func(add, 10, 20)
    print(f"执行结果：{result}")  # 输出：准备执行函数：add → 执行结果：30



def calculate_salary(basic_salary :int ):
    def adder(perform_salary :int):
        return basic_salary + perform_salary
    print(f"total {adder(perform_salary=10000)}")
    return adder

def func_return_test():
    print('*' *50 ,'func_return_test', '*'*50)

    adder =calculate_salary(5000)
    print(adder(300))
    print(adder(400))
    print(adder(1000))
    print(calculate_salary(7000)(-1000))
    print(calculate_salary(7000)(-2000))
    print(calculate_salary(7000)(-3000))




if __name__ == '__main__':
    normal_func()
    func_param_test()
    func_return_test()
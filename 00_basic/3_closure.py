# 定义需要被增强的原函数
import time


def add2(a, b):
    return a + b


def add4(a, b, c, d):
    return a + b + c + d


def mul(a, b, c, d, e, f):
    return a * b * c * d * e * f


def sum_multi(*args ):
    sum_res = 0
    for arg in args:
        sum_res =sum_res + arg
    return sum_res


# 定义一个“日志增强”的闭包（装饰器雏形）
def log_decorator(func):
    # 内层函数：增强原函数的功能
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"\nstart exec：func name: {func.__name__}, args: ",args)  # 新增功能：打印日志
        result = func(*args)  # 执行原函数（固定参数，不够灵活）
        end = time.time()
        print(f"函数 {func.__name__} 执行完成，结果：{result}, 执行时间：{end - start:.9f}秒" )
        return result
    return wrapper


print(f"sum_multi ===== start")
res = sum_multi(1,2,3,4,5,6,7,8,9,10,11,12)
print(f"sum_multi ===== {res}")
print(f"sum_multi ===== end")

print(log_decorator(sum_multi)(1,2,3,4,5,6,7,8,9,10,11,12))


@log_decorator
def multiply_multi(*args):
    time.sleep(1)
    mul_res = 1
    for arg in args:
        mul_res = mul_res*arg
    return mul_res


print(type(multiply_multi(1,2,3,4,5,6,7,8,9,10,11,12)))
print(multiply_multi(1,2,3,4,5,6,7,8,9,10,11,12))

exit(1)

# 用闭包增强add函数
enhanced_add = log_decorator(add2, 100, 200)
print(type(enhanced_add))
print(enhanced_add.__name__)
print(enhanced_add.__doc__)
# 执行增强后的函数
enhanced_add()
# 输出：
# 开始执行函数：add
# 函数 add 执行完成，结果：5

print('*' * 40, '以上函数先赋值 再 执行的方式相当于 以下方式')
log_decorator(add2, 100, 2002)()

print('*' * 40, '4 params ')
log_decorator(add4, 1, 2, 3, 4)()

print('*' * 40, '6 params ')
log_decorator(mul, 1, 2, 3, 4, 5, 6)()

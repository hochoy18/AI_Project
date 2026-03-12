import functools
import time


def log_decorator(level="INFO"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            print(f"[{level}] 开始执行函数：{func.__name__}, time:{start}")
            result = func(*args, **kwargs)
            end = time.time()
            print(f"[{level}] 函数 {func.__name__} 执行完成, time:{end}, duration:{(end-start)*1000:.2f} ms, result:{result}")
            return result
        return wrapper
    return decorator


@log_decorator("DEBUG")
def hello_world(*args ):
    time.sleep(2)
    hello = 0
    for arg in args:
        hello += arg
    return hello


print(hello_world(1,2,3,4,5))

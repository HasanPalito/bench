from memory_profiler import memory_usage
import functools

def memory_profiled(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        mem_usage = memory_usage((func, args, kwargs))
        result = func(*args, **kwargs)  
        print(f"Memory usage (MB): {mem_usage}")
        return result
    return wrapper

@memory_profiled
def example_function(n):
    return [i for i in range(n)]


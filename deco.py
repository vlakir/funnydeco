def benchmark(func):
    """
    Функция-декоратор, выводящая время выполнения декорируемой функции
    """
    import time

    def wrapper(*args, **kwargs):
        timer_start = time.perf_counter()
        result = func(*args, **kwargs)
        timer_stop = time.perf_counter()
        if kwargs.get('print_benchmark'):
            print(f'{kwargs.get("benchmark_name")}: время выполнения = '
                  f'{round((timer_stop - timer_start) * 1e3, 2)} мc')
        return result
    return wrapper


def singleton(class_):
    """
    Функция-декоратор, реализующая паттерн синглтон
    """
    singleton.instances = {}

    def getinstance(*args, **kwargs):
        if class_.__name__ not in singleton.instances:
            singleton.instances[class_.__name__] = class_(*args, **kwargs)
        return singleton.instances[class_.__name__]

    return getinstance

def benchmark(func):
    """
    Outputs the execution time of the decorated function.
    """
    import time

    def wrapper(*args, **kwargs):
        timer_start = time.perf_counter()
        result = func(*args, **kwargs)
        timer_stop = time.perf_counter()
        if kwargs.get('print_benchmark'):
            print(f'{kwargs.get("benchmark_name")}: execution time = '
                  f'{round((timer_stop - timer_start) * 1e3, 2)} ms')
        return result
    return wrapper


def singleton(class_):
    """
    Implements the singleton pattern
    """
    singleton.instances = {}

    def wrapper(*args, **kwargs):
        if class_.__name__ not in singleton.instances:
            singleton.instances[class_.__name__] = class_(*args, **kwargs)
        return singleton.instances[class_.__name__]

    return wrapper


class SingletonReseter:
    """
    Parent class for temporary stopping singleton behaviour
    """
    def reset_singleton(self) -> None:
        """
        Removes an instance of the class from the singleton decorator cache.
        The next created object will be initiated again.
        """
        self_name = self.__class__.__name__
        try:
            # noinspection PyUnresolvedReferences
            singleton.instances.pop(self_name)
        except KeyError:
            pass

# funnydeco
Collection of useful decorators for python projects
Implements:

1. Benchmarking util for methods
2. Singleton pattern for classes

____
##Examples:

###1. Benchmark decorators

```python
from funnydeco import benchmark


# noinspection PyUnusedLocal
@benchmark
def long_loop(print_benchmark=False, benchmark_name='') -> int:
    """
    Demo class for example of benchmark
    """
    result = 0
    for i in range(int(1e7)):
        result += i
    return result


if __name__ == '__main__':
    print('With benchmark:')
    long_loop(print_benchmark=True, benchmark_name='Long loop procedure')
    print('Without benchmark:')
    long_loop()
```
    
###2. Singleton decorators

```python
from funnydeco import singleton, SingletonReseter
from time import sleep


@singleton
class SlowInitClass(SingletonReseter):
    """
    Demo class for example of singleton decorator
    """

    def __init__(self):
        self.variable = 100
        print("I'm sleeping...")
        sleep(5)
        print("I'v woken up")


if __name__ == '__main__':
    print('First dumbass init:')
    dumbass1 = SlowInitClass()
    print(dumbass1.variable)
    print()

    print('Second dumbass init:')
    dumbass2 = SlowInitClass()
    print(dumbass2.variable)
    print()

    print('Third dumbass init:')
    print('Temporary stopping singleton behaviour')
    SlowInitClass().reset_singleton()
    dumbass3 = SlowInitClass()
    print(dumbass2.variable)
    print()

    print('Fourth dumbass init:')
    dumbass4 = SlowInitClass()
    print(dumbass4.variable)
    print()
```

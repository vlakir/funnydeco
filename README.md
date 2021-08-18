# funnydeco
Collection of useful decorators for python projects
Implements:

1. Benchmarking util for methods
2. Singleton pattern realisation for classes

____
## Installation:
```
pip install funnydeco
```
____
## Examples:

### 1. Benchmark decorator

```python
from funnydeco.core import singleton, SingletonReseter
from time import sleep


@singleton
class SlowInitClass(SingletonReseter):
    """
    Demo class for example of singleton decorator
    """
    def __init__(self):
        self.variable = 1
        print("I'm sleeping...")
        sleep(3)
        print("I'v woken up!")


if __name__ == '__main__':
    print('First dumbass init:')
    dumbass1 = SlowInitClass()
    print(f'variable={dumbass1.variable}')
    dumbass1.variable = 2

    print()

    print('Second dumbass init:')
    dumbass2 = SlowInitClass()
    print(f'variable={dumbass2.variable}')
    print()

    print('Third dumbass init:')
    print('Temporary stopping singleton behaviour')
    SlowInitClass().reset_singleton()
    dumbass3 = SlowInitClass()
    print(f'variable={dumbass3.variable}')
    dumbass3.variable = 3
    print()

    print('Fourth dumbass init:')
    dumbass4 = SlowInitClass()
    print(f'variable={dumbass4.variable}')
    print()
```

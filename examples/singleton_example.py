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

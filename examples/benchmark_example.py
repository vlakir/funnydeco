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

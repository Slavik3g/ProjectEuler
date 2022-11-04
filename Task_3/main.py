import math


def issimple(number: int) -> int:
    max_divider = 0
    for i in range(2, math.ceil(math.sqrt(number))):
        if number % i == 0:
            if issimple(i) == 0:
                max_divider = i
    return 0 if max_divider == 0 else max_divider


def run():
    print(issimple(600851475143))


if __name__ == '__main__':
    run()

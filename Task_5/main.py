def compute(range_limit: int) -> int:
    number = range_limit
    for i in range(2, range_limit + 1):
        if number % i != 0:
            temp = number
            while number % i != 0:
                number += temp
    return number


def run():
    print(compute(20))


if __name__ == '__main__':
    run()

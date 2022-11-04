def compute(max_number: int) -> int:
    a, b = 1, 1
    res = 0
    while a < max_number:
        a, b = a + b, a
        if a % 2 == 0:
            res += a
    return res


def run():
    print(compute(4_000_000))


if __name__ == '__main__':
    run()


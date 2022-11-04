def compute(below_num: int) -> int:
    return sum(i for i in range(1, below_num) if i % 3 == 0 or i % 5 == 0)


def run():
    print(compute(1000))


if __name__ == '__main__':
    run()

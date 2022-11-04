def compute(range_limit: int) -> int:
    return int((range_limit*(range_limit - 1) * (range_limit + 1) * (3*range_limit + 2))/12)


def run():
    print(compute(100))


if __name__ == '__main__':
    run()

from decorator import decorator


@decorator
def print_surprise(_, *__, **___):
    print("surprise !")


@decorator
def execute_twice(func, *args, **kwargs):
    func(*args, **kwargs)
    func(*args, **kwargs)


@execute_twice
@print_surprise
def test_func(a, b, c):
    print(a+b+c)


def main():
    test_func(1, 2, 5)


if __name__ == "__main__":
    main()

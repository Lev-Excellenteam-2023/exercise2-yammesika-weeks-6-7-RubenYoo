def type_check(correct_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if all(isinstance(arg, correct_type) for arg in args):
                return func(*args, **kwargs)
            else:
                raise TypeError(f"All arguments must be of type {correct_type.__name__}")
        return wrapper
    return decorator


@type_check(int)
def times2(number):
    return number * 2


def main():
    try:
        print(times2(8))
        print(times2('a'))
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()

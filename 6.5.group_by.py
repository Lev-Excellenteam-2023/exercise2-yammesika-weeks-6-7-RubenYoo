def group_by(func, iterable):
    return {func(key): [value for value in iterable if func(key) == func(value)] for key in iterable}


def main():
    print(group_by(len, ["hi", "bye", "yo", "try"]))


if __name__ == "__main__":
    main()


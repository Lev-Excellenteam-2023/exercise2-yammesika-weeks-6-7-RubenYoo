import time


def timer(f, *args, **kwargs):
    t1 = time.time()
    f(*args, **kwargs)
    return time.time() - t1


print(timer(print, "Hello"))
print(timer(zip, [1, 2, 3], [4, 5, 6]))
print(timer("Hi {name}".format, name="Bug"))

print(timer(pow, 5, 5689179))

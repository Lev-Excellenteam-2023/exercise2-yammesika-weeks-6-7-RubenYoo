def group_by(func, it):
    return {func(i): [j for j in it if func(i) == func(j)] for i in it}


print(group_by(len, ["hi", "bye", "yo", "try"]))

def facto(n):
    if n == 0:
        return 1
    return n * facto(n - 1)


def recursive_linear(a, i) -> int:
    if not len(a):
        return False
    last = a.pop()
    if last == i:
        return True
    else:
        return recursive_linear(a, i)


def recursive_linear_alt(a, i) -> int:
    if not len(a):
        return False
    first = a.pop(0)
    if first == i:
        return True
    else:
        return recursive_linear(a, i)

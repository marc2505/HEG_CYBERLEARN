def f(x: int) -> int:
    x = x + 1

    print("dans f(x): x =", x)
    return x


x: int = 3
z: int = f(x)

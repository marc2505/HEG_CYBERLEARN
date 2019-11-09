""" algo: portée
"""


def g():
    x: int = 30
    print("g:", x)


def f():
    x: int = 20
    print("f:", x)


### programme principal
x: int = 10
f()
g()
print("p:", x)

class Arxitektor:
    def __init__(self, ism):
        self.ism = ism

    def metod(self, a, b):
        return a + b

    def metod(self, a, b, c):
        return a + b + c

arxitektor = Arxitektor("Ali")
print(arxitektor.metod(1, 2))  # 3
print(arxitektor.metod(1, 2, 3))  # 6
```

```python
class Arxitektor:
    def __init__(self, ism):
        self.ism = ism

    def metod(self, *args):
        return sum(args)

arxitektor = Arxitektor("Ali")
print(arxitektor.metod(1, 2))  # 3
print(arxitektor.metod(1, 2, 3))  # 6
```

```python
class Arxitektor:
    def __init__(self, ism):
        self.ism = ism

    def metod(self, a, b, c=None, d=None):
        if c is None and d is None:
            return a + b
        elif c is not None and d is None:
            return a + b + c
        else:
            return a + b + c + d

arxitektor = Arxitektor("Ali")
print(arxitektor.metod(1, 2))  # 3
print(arxitektor.metod(1, 2, 3))  # 6
print(arxitektor.metod(1, 2, 3, 4))  # 10

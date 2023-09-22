


class Jar:
    def __init__(self, capacity=12):
        if int(capacity) < 0:
            raise ValueError("Capacity can't be negative")
        else:
            self.capacity = capacity
            self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if size + n > capacity:
            raise ValueError("Too many cookies")
        else:
            size += n

    def withdraw(self, n):
        if size

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
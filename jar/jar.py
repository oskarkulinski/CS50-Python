
def main():
    j = Jar(15)
    j.deposit(5)
    print(j)

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
        if self.size + n > self.capacity:
            raise ValueError("Too many cookies")
        else:
            self.size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Not enough cookies")
        else:
            self.size -=n

    @setter
    def capacity(self):
        

    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        return self.size


if __name__ == "__main__":
    main()
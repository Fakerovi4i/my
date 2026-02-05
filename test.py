
class SquareIterator:
    def __init__(self, n):
        self.__n = n
        self.__start = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.__start <= self.__n:
            value = self.__start ** 2
            self.__start += 1
            return value
        raise StopIteration

# Должно работать:
my = SquareIterator(4)

print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))

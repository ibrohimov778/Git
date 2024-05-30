# Iterable => list , tuple , dict
# Iterator
from typing import List


# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')


# number = 5
# while number > 0:
#     name = 'Ali'
#     print(f'Hello => {name}')
#     number -= 1

#
# for i in range(1, 10, 2):  # start , stop , step
#     print(i)

# arr = [10, 20, 30, 40]
# iterator = iter(arr)
#
# while True:
#     try:
#         print(next(iterator))
#     except StopIteration as e:
#         break

#
class Sequence:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._sequence):
            raise StopIteration
        else:
            result = self._sequence[self._index]
            self._index += 1
            return result


arr = ['a', 'b', 'c', 'd']
sequences = Sequence(arr)
print(next(sequences))
print(next(sequences))
print(next(sequences))
print(next(sequences))
print(next(sequences))
# for item in sequences:
#     print(item)


# arr = [10, 20, 30, 40, 50]
# new_arr = iter(arr)
# print(dir(new_arr))
# print(dir(arr))
# seq = Sequence(arr)
# print(next(seq))
# print(next(seq))
# print(next(seq))
# print(next(seq))
# print(next(seq))
# print(next(seq))
# while True:
#     try:
#         print(next(seq))
#     except StopIteration:
#         break


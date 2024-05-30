import os
from contextlib import contextmanager


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('Simple-Dir-One'):
    print(os.listdir())
with change_dir('Simple-Dir-Two'):
    print(os.listdir())
class Filemanager():
    def __init_(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exti__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


# loading a file
with Filemanager('test.txt', 'w') as f:
    f.write('Testing two')
print(f.closed)
f = open('test.txt.txt', 'w')
f.write('Testing')
f. close()
with open('test.txt', 'w') as f:
    f.write('Testing')
class OpenFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def _enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


with OpenFile('test.txt', 'W') as f:
    f.write('Testing')

print(f.closed)



import os


cwd = os.getcwd()   # get current working directory
os.chdir('directory_1')  # changing directory
print(os.listdir())     # listing files
os.chdir(cwd)   # changing directory back to current

cwd = os.getcwd()
os.chdir('directory_2')
print(os.listdir())
os.chdir(cwd)

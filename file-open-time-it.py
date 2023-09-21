import timeit
from memory_profiler import profile

setup = '''
file_path = "shakespeare.txt"

def test1(file_path):
    with open(file_path, "r", encoding="utf-8") as file_in:
        return [line for line in file_in]

def test2(file_path):
    return [line for line in open(file_path, "r", encoding="utf-8")]

def test3(file_path):
    with open(file_path, "r", encoding="utf-8") as file_in:
        return file_in.readlines()

def test4(file_path):
    with open(file_path, "r", encoding="utf-8") as file_in:
        return list(file_in)

def test5(file_path):
    with open(file_path, "r", encoding="utf-8") as file_in:
        yield from file_in
'''

print(timeit.timeit("test1(file_path)", setup=setup, number=100))
print(timeit.timeit("test2(file_path)", setup=setup, number=100))
print(timeit.timeit("test3(file_path)", setup=setup, number=100))
print(timeit.timeit("test4(file_path)", setup=setup, number=100))
print(timeit.timeit("list(test5(file_path))", setup=setup, number=100))

file_path = "shakespeare.txt"

@profile
def test1(file_path):
    with open(file_path, "r", encoding="utf-8") as file_in:
        return [line for line in file_in]

@profile
def test2(file_path):
    return [line for line in open(file_path, "r", encoding="utf-8")]

@profile
def test3(file_path):
    with open(file_path, "r", encoding="utf-8") as file_in:
        return file_in.readlines()

@profile
def test4(file_path):
    with open(file_path, "r", encoding="utf-8") as file_in:
        return list(file_in)

@profile
def test5(file_path):
    with open(file_path, "r", encoding="utf-8") as file_in:
        yield from file_in

test1(file_path)
test2(file_path)
test3(file_path)
test4(file_path)
list(test5(file_path))

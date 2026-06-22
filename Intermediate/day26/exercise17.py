with open('file1.txt') as f:
    set_one = [int(n) for n in f.readlines()]


with open('file2.txt') as f:
    set_two = [int(n) for n in f.readlines()]


result = [n for n in set_one if n in set_two]

print(result)

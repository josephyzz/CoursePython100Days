lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(filter(lambda n: n % 2 == 0, lista)))
print([n for n in lista if n % 2 == 0])

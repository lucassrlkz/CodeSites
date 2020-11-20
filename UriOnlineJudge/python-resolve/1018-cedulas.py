entry, notas = int(input()), [100, 50, 20, 10, 5, 2, 1]
print(entry)

for nota in notas:
    qtde = int(entry/nota)
    print("{0} nota(s) de R$ {1},00".format(qtde, nota))
    entry %= nota

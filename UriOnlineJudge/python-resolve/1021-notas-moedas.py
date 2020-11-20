entry, notas = float(input()), [100, 50, 20, 10, 5, 2]
moedas = [1, .5, .25, .1, .05, .01]

print('NOTAS:')
for nota in notas:
    qtde = int(entry/nota)
    print("{} nota(s) de R$ {:.2f}".format(qtde, nota))
    entry %= nota

print('MOEDAS:')
for moeda in moedas:
    qtde = int(round(entry, 2)/moeda)
    print("{} moeda(s) de R$ {:.2f}".format(qtde, moeda))
    entry %= moeda

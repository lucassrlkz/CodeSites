entry, n_achou, res = float(input()), True, ''

if(entry < 0 or entry > 100):
    res += 'Fora de intervalo'
    n_achou = False

elif(entry <= 25.00 and n_achou):
    res += 'Intervalo [0,25]'
    n_achou = False

elif(entry <= 50.0 and n_achou):
    res += 'Intervalo (25,50]'
    n_achou = False

elif(entry <= 75.0 and n_achou):
    res += 'Intervalo (50,75]'
    n_achou = False

elif(entry <= 100.0 and n_achou):
    res += 'Intervalo (75,100]'
    n_achou = False

print(res)

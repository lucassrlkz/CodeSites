i, f = list(map(int, input().split()))

t = f-i if i < f else (24-i)+f
print("O JOGO DUROU {} HORAS(S)".format(t))

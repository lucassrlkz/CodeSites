entry = input().split()
a, b = map(int, entry)

if (b % a == 0) or (a % b == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

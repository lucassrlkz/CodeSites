origem = list(map(int, input().split()))
sortlist = origem.copy()

sortlist.sort()

for i in sortlist:
    print(i)

print("")

for n in origem:
    print(n)

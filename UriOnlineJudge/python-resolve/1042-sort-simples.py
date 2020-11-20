entry = input().split(" ")
origem = [int(entry[0]), int(entry[1]), int(entry[2])]
sortlist = origem.copy()

sortlist.sort()

for i in sortlist:
    print(i)

print("")

for n in origem:
    print(n)

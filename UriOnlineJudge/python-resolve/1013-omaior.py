entry = input().split()
a, b, c = int(entry[0]), int(entry[1]), int(entry[2])

m1 = (a + b + abs(a-b)) / 2

print(f"%.3f eh o maior" % ((m1 + c + abs(m1-c)) / 2))

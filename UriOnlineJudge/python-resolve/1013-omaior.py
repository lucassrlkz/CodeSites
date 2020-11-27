a, b, c = list(map(float, input().split()))

m1 = (a + b + abs(a-b)) / 2

print(f"%.3f eh o maior" % ((m1 + c + abs(m1-c)) / 2))

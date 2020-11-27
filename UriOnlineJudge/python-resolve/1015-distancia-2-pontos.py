import math

p1, p2 = input().split(), input().split()

x1, y1 = list(map(float, p1))
x2, y2 = list(map(float, p2))

print(f"%.4f" % math.sqrt((x2-x1)**2 + (y2 - y1)**2))

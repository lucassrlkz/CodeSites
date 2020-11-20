import math

p1, p2 = input().split(), input().split()

x1, y1 = float(p1[0]), float(p1[1])
x2, y2 = float(p2[0]), float(p2[1])

print(f"%.4f" % math.sqrt((x2-x1)**2 + (y2 - y1)**2))

# entry 3.0 / 4.0 / 5.2
a, b, c = list(map(float, input().split()))
pi, dots = 3.14159, ": "

print(f"TRIANGULO{dots}%.3f" % ((a*c)/2))

print(f"CIRCULO{dots}%.3f" % (pi * (c**2)))

print(f"TRAPEZIO{dots}%.3f" % (c*(a+b)/2))

print(f"QUADRADO{dots}%.3f" % (b*b))

print(f"RETANGULO{dots}%.3f" % (a*b))

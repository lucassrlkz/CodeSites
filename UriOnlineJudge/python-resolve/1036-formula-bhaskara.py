import math

a, b, c = list(map(float, input().split()))

if a == 0.0 or (b**2 - 4*a*c) < 0:
    print("Impossivel calcular")
else:
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

    print(f"R1 = %.5f" % x1)
    print(f"R2 = %.5f" % x2)

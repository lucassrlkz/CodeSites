entry = input().split()
entry = list(map(float, entry))
a, b, c = entry

if (a+b > c and b+c > a and a+c > b):
    print("Perimetro = %.1f" % (a+b+c))
else:
    print("Area = %.1f" % (0.5*(a+b)*c))

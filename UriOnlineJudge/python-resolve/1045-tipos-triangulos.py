a, b, c = sorted(map(float, input().split()), reverse=True)

cal = b+c

if a >= cal:
    print("NAO FORMA TRIANGULO")
else:
    cal2 = (b**2) + (c**2)
    if (a**2) == cal2:
        print("TRIANGULO RETANGULO")

    elif (a**2) > cal2:
        print("TRIANGULO OBTUSANGULO")

    elif (a**2) < cal2:
        print("TRIANGULO ACUTANGULO")

if a == b == c:
    print("TRIANGULO EQUILATERO")

if a == b != c or b == c != a or a == c != b:
    print("TRIANGULO ISOSCELES")

a, b, c, d = list(map(int, input().split()))

if b > c and d > a:
    cd = c+d
    ab = a+b
    if cd > ab:
        if c >= 0 and d >= 0:
            if a % 2 == 0:
                print("Valores aceitos")
            else:
                print("Valores nao aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")

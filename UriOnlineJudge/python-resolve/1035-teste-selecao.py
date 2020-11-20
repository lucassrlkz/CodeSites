entry = input().split()
a, b, c, d = int(entry[0]), int(entry[1]), int(entry[2]), int(entry[3])

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

entry = input().split()
origem, x, y = 0, float(entry[0]), float(entry[1])


if x == origem:
    if y == origem:
        print("Origem")

    if y != origem:
        print('Eixo Y')


elif y == origem:
    if x != origem:
        print("Eixo X")

if x > origem:
    if y > origem:
        print("Q1")

    if y < origem:
        print("Q4")

if x < origem:
    if y > origem:
        print("Q2")

    if y < origem:
        print("Q3")

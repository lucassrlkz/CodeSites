tabela = [1, 4], [2, 4.5], [3, 5], [4, 2], [5, 1.5]

entry = input().split(' ')
id, price = int(entry[0]), int(entry[1])

for val in tabela:
    if id == val[0]:
        print('Total: R$ {:.2f}'.format((val[1]*price)))

entry, ano, mes = int(input()), 365, 30

if entry >= ano:
    aux = int(entry // ano)
    print('{} ano(s)'.format(aux))
    entry = entry - ano * aux

elif entry < ano:
    print('{} ano(s)'.format(0))

if entry >= mes:
    aux = int(entry // mes)
    print('{} mes(es)'.format(aux))

    entry = entry - mes * aux
    print('{} dia(s)'.format(entry))

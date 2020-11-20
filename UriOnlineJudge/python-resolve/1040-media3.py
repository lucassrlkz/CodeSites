entry = input().split()
res_nota, res_peso, pesos = 0, 0, [2, 3, 4, 1]

notas = [(float(entry[0])*pesos[0]), (float(entry[1])*pesos[1]),
         (float(entry[2])*pesos[2]), (float(entry[3])*pesos[3])]

for peso in pesos:
    res_peso += peso

for nota in notas:
    res_nota += nota

msg = ''
media = res_nota/res_peso
msg = 'Media: {:.1f}'.format(media)
print(msg)

if media >= 7.0:
    msg = 'Aluno aprovado.'
    print(msg)

elif media < 5.0:
    msg = 'Aluno reprovado.'
    print(msg)

elif media >= 5.0 and media <= 6.9:
    print('Aluno em exame.')
    n_exame = float(input())

    print('Nota do exame: {:.1f}'.format(n_exame))
    media = (media+n_exame)/2

    if media >= 5.0:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(media))

    elif media <= 4.9:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(media))

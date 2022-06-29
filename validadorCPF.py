while True:
    while True:
        cpf = input('Digite o CPF sem ponto e traço para validação: ')
        if not cpf.isnumeric() or len(cpf) != 11:
            print('Voce nao digitou o CPF corretamente.')
        else:
            break

    r = 10
    novo_cpf = cpf[:-2]
    t = 0

    for i in range(19):
        if i > 8:
            i -= 9

        t += int(novo_cpf[i]) * r

        r -= 1
        if r < 2:
            r = 11
            d = 11 - (t % 11)

            if d > 9:
                d = 0
            t = 0
            novo_cpf += str(d)
    if novo_cpf == cpf:
        print('O CPF digitado e válido. ')
    else:
        print('O CPF digitado e inválido. ')

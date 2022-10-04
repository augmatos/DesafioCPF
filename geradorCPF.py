from random import randint


def gera_cpf():
    numero = str(randint(100000000, 999999999))

    r = 10
    novo_cpf = numero
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
    l1 = novo_cpf[0:3]
    l2 = novo_cpf[3:6]
    l3 = novo_cpf[6:9]
    digito = novo_cpf[9:11]
    return novo_cpf

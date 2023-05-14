print("Bem vindo a Lanchonete do Lucas Lima de Ávila")
print("**********Cardápio**********")
print("|Código|    Descrição          | Valor |")
print("|  100 |    Cachorro Quente    |  9,00 |")
print("|  101 | Cachorro Quente Duplo | 11,00 |")
print("|  102 |    X-Egg              | 12,00 |")
print("|  103 |    X-Salada           | 12,00 |")
print("|  104 |    X-Bacon            | 14,00 |")
print("|  105 |    X-Tudo             | 17,00 |")
print("|  200 |    Refrigerante Lata  |  5,00 |")
print("|  201 |    Chá Gelado         |  4,00 |")
total = 0

while True:
    codigo = int(input("Entre com o código desejado: "))
    if codigo != 100 and codigo != 101 and codigo != 102 and codigo != 103 and codigo != 104 and codigo != 105 and codigo != 200 and codigo != 201:
        print("Opção Inválida")
        continue

    if codigo == 100:
        valor = 9.0
        total += valor
        print("Você pediu um Cachorro-Quente no valor de 9,00")

    elif codigo == 101:
        valor = 11.0
        total += valor
        print("Você pediu um Cachorro-Quente Duplo no valor de 11,00")

    elif codigo == 102:
        valor = 12.0
        total += valor
        print("Você pediu um X-Egg no valor de 12,00")

    elif codigo == 103:
        valor = 13.0
        total += valor
        print("Você pediu um X-Salada no valor de 13,00")

    elif codigo == 104:
        valor = 14.0
        total += valor
        print("Você pediu um X-Bacon no valor de 14,00")

    elif codigo == 105:
        valor = 17.0
        total += valor
        print("Você pediu um X-Tudo no valor de 17,00")

    elif codigo == 200:
        valor = 5.0
        total += valor
        print("Você pediu um Refrigerante lata no valor de 5,00")

    elif codigo == 201:
        valor = 4.0
        total += valor
        print("Você pediu um Chá Gelado no valor de 4,00")

    adicional = int(input("Deseja pedir mais alguma coisa?\n"
                          "1 - Sim\n"
                          "0 - Não\n"
                          " "))
    if adicional == 1:
        continue
    else:
        if adicional == 0:
            break
print(f"O total a ser pago é: {total:.2f}")
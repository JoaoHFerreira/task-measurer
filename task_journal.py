import datetime


def cabec(val1, val2):  # hora de início do colaborador, hh/mm
    if val1 < 10:
        val1 = "0" + str(val1) + ":"
    else:
        val1 = str(val1) + ":"
    if val2 < 10:
        val2 = "0" + str(val2)
    else:
        val2 = str(val2)
    return val1, val2


def ApEst(val1, val2):  # Apontamento estático
    print("\n\n", "Tempo da atividade em horas")
    dh = int(input())  # duração horas
    if dh > 12:
        while dh > 12:
            print(
                "As atividades devem ser detalhadas não podendo ser iguais ou maiores a 12 horas"
            )
            print("\n\n", "Tempo da atividade em horas")
            dh = int(input())  # duração horas
    dh = dh + val1
    print("\n\n", "Tempo da atividade em minutos")
    dm = int(input())  # duração minutos
    if dm > 59:
        while dm > 59:
            print("O tempo máximo em minutos eh '59'")
            print("\n\n", "Tempo da atividade em minutos")
            dm = int(input())  # duração minutos
    dm = dm + val2
    if dm > 59:
        dh = dh + 1
        dm = dm - 60
    return dh, dm


def ApDin():
    now = datetime.datetime.now()
    dh, dm = now.hour, now.minute
    return dh, dm


def fill(f, val1, val2):  # hr, min
    op = 0
    # Enquanto não for preenchido com valor certo, loop
    while op != 1 or op != 2:
        print("\n\n|-------------------------------------|")
        print("|Digite 1 para apontar dinamicamente  |")
        print("|Digite 2 para apontar estaticamente|")
        print("|-------------------------------------|\n\n")
        op = int(input())
        if op == 1:
            dh, dm = ApDin()
            break
        elif op == 2:
            dh, dm = ApEst(val1, val2)
            break
    print("\n\n", "Digite uma breve descrição da atividade:")
    av = input(str())  # atividade
    dh, dm = cabec(dh, dm)
    val1, val2 = cabec(val1, val2)
    f.write(val1 + val2 + " - " + dh + dm + " -- " + av + "\n")


def read(val1, val2):  # nome do arquivo, valor inicial da string, valor final da string
    name = MontaTitulo()
    f = open(name, "r")

    value = int(f.readlines()[-1][val1:val2])  # valor ultima hora
    f.close
    return value


def MontaTitulo():
    now = datetime.datetime.now()
    a = "agenda"
    y, m, d, h, mn = now.year, now.month, now.day, now.hour, now.minute
    dv = [y, m, d]  # DataValue
    for i in range(len(dv)):
        dv[i] = str(dv[i])
    name = a + "." + dv[0] + "." + dv[1] + "." + dv[2] + ".txt"
    return name


def visu():
    name = MontaTitulo()
    try:
        f = open(name, "r")
        print("\n\n")
        for i in f.readlines():
            print(i)
        f.close
    except FileNotFoundError as x:
        print("\n\nNÃO EXISTEM REGISTROS")
    print("\n\n")
    print("\n\n|-------------------------------------------------|")
    print("|Digite 1 para finalizar                           |")
    print("|Digite outro número para voltar ao menu principal |")
    print("|-------------------------------------------------|\n\n")
    op = int(input())
    if op == 1:
        exit()
    else:
        menu()


def main():
    name = MontaTitulo()
    try:
        f = open(name, "x")
        print("Digite hora de inicio do trabalho:")
        hin = int(input())
        print("\n\n", "Digite minutos de inicio do trabalho:")
        minn = int(input())
        fill(f, hin, minn)  # Hora de início padrão//(hora,minutos)
    except FileExistsError as x:
        vh = read(8, 10)  # posição da ultima hora
        vm = read(11, 13)  # posição do ultimo minuto
        f = open(name, "a")
        fill(f, vh, vm)
    f.close


def menu():
    print("\n\n|-------------------------------------|")
    print("|Digite 1 para apontar horas          |")
    print("|Digite 2 para visualizar apontamentos|")
    print("|Digite 3 para instruções             |")
    print("|Digite 4 para sair                   |")
    print("|-------------------------------------|\n\n")

    op = int(input())
    if op != 4:
        while op != 4:
            if op == 1:
                main()
            elif op == 2:
                visu()
            menu()
    else:
        exit()


menu()

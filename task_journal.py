import msgs
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
    msgs.total_time_in_hours()
    dh = int(input())  # duração horas
    if dh > 12:
        while dh > 12:
            msgs.activity_max_time()
            msgs.total_time_in_hours()
            dh = int(input())  # duração horas
    dh = dh + val1
    msgs.total_time_in_minutes()
    dm = int(input())  # duração minutos
    if dm > 59:
        while dm > 59:
            msgs.max_time_in_minutes()
            msgs.total_time_in_minutes()
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
        msgs.dynamic_or_static_menu()
        op = int(input())
        if op == 1:
            dh, dm = ApDin()
            break
        elif op == 2:
            dh, dm = ApEst(val1, val2)
            break
    msgs.activity_description()
    av = input(str())  # atividade
    dh, dm = cabec(dh, dm)
    val1, val2 = cabec(val1, val2)
    f.write(val1 + val2 + " - " + dh + dm + " -- " + av + "\n")


# nome do arquivo, valor inicial da string, valor final da string
def read(val1, val2):
    name = MontaTitulo()
    f = open(name, "r")

    value = int(f.readlines()[-1][val1:val2])  # valor ultima hora
    f.close
    return value


def MontaTitulo():
    now = datetime.datetime.now()
    a = "agenda"
    y, m, d = now.year, now.month, now.day
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
        print(f"\n\nNÃO EXISTEM REGISTROS de {x}")
    msgs.roll_back_menu()
    op = int(input())
    if op == 1:
        exit()
    else:
        main()


def menu():
    name = MontaTitulo()
    try:
        f = open(name, "x")
        msgs.hour_init_time()
        hin = int(input())
        msgs.minutes_init_time()
        minn = int(input())
        fill(f, hin, minn)  # Hora de início padrão//(hora,minutos)
    except FileExistsError as x:
        print(f"\n\nArquivo {x} já existe")
        vh = read(8, 10)  # posição da ultima hora
        vm = read(11, 13)  # posição do ultimo minuto
        f = open(name, "a")
        fill(f, vh, vm)
    f.close


def main():
    msgs.main_menu()
    op = int(input())
    if op != 4:
        while op != 4:
            if op == 1:
                menu()
            elif op == 2:
                visu()
            main()
    else:
        exit()


if __name__ == "__main__":
    main()

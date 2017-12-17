import datetime

def cabec(val1,val2):#hora de início do colaborador, hh/mm
        if val1<10:
            val1="0"+str(val1)+":"
        else:
            val1=str(val1)+":"
        if val2<10:
            val2="0"+str(val2)
        else:
            val2=str(val2)
        return val1, val2

def fill(f,val1,val2): #hr, min
    print("\n\n","Digite uma breve descrição da atividade:")
    av=input(str()) #atividade
    print("\n\n","Tempo da atividade em horas")
    dh=int(input()) #duração horas
    dh=dh+val1
    print("\n\n","Tempo da atividade em minutos")
    dm=int(input()) #duração minutos
    dm=dm+val2
    dh,dm=cabec(dh,dm)
    val1,val2=cabec(val1,val2)
    f.write(val1+val2+" - "+dh+dm+" -- "+av+"\n")

def read(val1, val2):# nome do arquivo, valor inicial da string, valor final da string
    name=MontaTitulo()
    f=open(name,"r")
    value=int(f.readlines()[-1][val1:val2] ) #valor ultima hora
    f.close
    return value

def MontaTitulo():
    now=datetime.datetime.now()
    a="agenda"
    y,m,d,h,mn=now.year, now.month, now.day, now.hour, now.minute
    dv=[y,m,d] #DataValue
    for i in range(len(dv)):
        dv[i]=str(dv[i])
    name=a+"."+dv[0]+"."+dv[1]+"."+dv[2]+".txt"
    return name


def main():
    name=MontaTitulo()
    try:
        f=open(name,"x")
        fill(f,8,0) #Hora de início padrão//(hora,minutos)
    except FileExistsError as x:
        vh=read(name,8,10) #valor da ultima hora
        vm=read(name,11,13)#valor do ultimo minuto
        f=open(name,"a")
        fill(vh,vm)
    f.close

def visu():
    name=MontaTitulo()
    f=open(name,"r")
    for i in f.readlines():
        print (i)
    f.close



def menu():
    print("|-------------------------------------|")
    print("|Digite 1 para apontar horas          |")
    print("|Digite 2 para visualizar apontamentos|")
    print("|Digite 3 para instruções             |")
    print("|Digite 4 para sair                   |")
    print("|-------------------------------------|\n\n")

    op=int(input())
    if op==1:
        main()
    elif op==2:
        visu()
    else:
        exit()

menu()

print("O programa calcula a idade de alguém em anos, meses e dias.")
print("====================================================================")

# ENTRADA
diaNasc = int(input("Digite o dia de nascimento: "))
mesNasc = int(input("Digite o mês de nascimento: "))
anoNasc = int(input("Digite o ano de nascimento: "))

diaHoje = int(input("Digite o dia atual: "))
mesHoje = int(input("Digite o mês atual: "))
anoHoje = int(input("Digite o ano atual: "))

# VARIÁVEIS
anosDeVida = anoHoje - anoNasc
mesesDeVida = 0
diasDeVida = 0

# AJUSTE DO ANO CASO AINDA NÃO TENHA FEITO ANIVERSÁRIO
if (mesHoje < mesNasc) or (mesHoje == mesNasc and diaHoje < diaNasc):
    anosDeVida = anosDeVida - 1

# MESES
if mesHoje >= mesNasc:
    mesesDeVida = mesHoje - mesNasc
else:
    mesesDeVida = (12 - mesNasc) + mesHoje

# DIAS
if diaHoje < diaNasc:
    mesesDeVida = mesesDeVida - 1

    # Descobre o mês anterior
    mesAnterior = mesHoje - 1
    anoRef = anoHoje
    if mesAnterior == 0:
        mesAnterior = 12
        anoRef = anoRef - 1

    # Descobre dias do mês anterior
    if mesAnterior == 1 or mesAnterior == 3 or mesAnterior == 5 or mesAnterior == 7 or mesAnterior == 8 or mesAnterior == 10 or mesAnterior == 12:
        diasNoMes = 31
    elif mesAnterior == 4 or mesAnterior == 6 or mesAnterior == 9 or mesAnterior == 11:
        diasNoMes = 30
    elif mesAnterior == 2:
        if (anoRef % 400 == 0) or (anoRef % 4 == 0 and anoRef % 100 != 0):
            diasNoMes = 29
        else:
            diasNoMes = 28

    diasDeVida = (diasNoMes - diaNasc) + diaHoje
else:
    diasDeVida = diaHoje - diaNasc

# SAÍDA
print("====================================================================")
print("A pessoa nasceu em", diaNasc, "/", mesNasc, "/", anoNasc, "e hoje é", diaHoje, "/", mesHoje, "/", anoHoje)
print("Idade:", anosDeVida, "anos,", mesesDeVida, "meses e", diasDeVida, "dias")
print("====================================================================")

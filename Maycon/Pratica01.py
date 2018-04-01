imposto = float(input("Digite o valor do imposto a ser calculado: "))
meses = int(input("Digite a quantidade de meses: "))

if imposto <= 100:
    multa = (imposto*4)/100
    total = imposto+multa

if imposto <= 200:
    multa = (imposto*7)/100
    total = imposto+multa

if imposto >= 300:
    multa = (imposto*10)/100
    total = imposto+multa

if meses >= 5 and imposto > 1:
    multa = (imposto*15)/100
    total = imposto+multa

    print("O valor do imposto é de: ", imposto)
    print("O valor da multa é de: ", multa)
    print("O valor final do imposto é de: ", total)

salario = float (input('Para conocer tu incremento salarial, ingresa tu salario actual:'))
if salario <= 15000:
    print('Tu incremento salarial es del 20%')
    print ('Tu nuevo salario es de:', salario * 0.20 + salario)
elif salario > 15000:
    print('Tu incremento salarial es del 15%')
    print ('Tu nuevo salario es de:', salario * 0.15 + salario)

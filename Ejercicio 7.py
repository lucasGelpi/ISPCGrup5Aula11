def ej7(tupla):
    print("Calculo promedio gastos de Lennon")
    total = 0
    gastos = 0
    for j in tupla:
        total += j
        gastos += 1
    promedio = round(total / gastos, 2)
    print('Total: ', total, ' pesos')
    if promedio > 4500:
        print('Promedio de gastos: ', promedio)
        print('Se ha excedido del gasto promedio para su mascota')
    else:
        print('Promedio de gastos: ', promedio)

if __name__ == '__main__':
    Historial3 = (9530, 4120, 4580, 1500, 890, 7516, 426,)
    ej7(Historial3)


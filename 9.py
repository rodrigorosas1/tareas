#ejercicio 9
altura = int(input("Introduce un número entero para la altura del triángulo: "))
for i in range(1, altura + 1):
    line = []
    for j in range(i):
        line.append(str(2 * (i - j) - 1))
    print(' '.join(line))
    

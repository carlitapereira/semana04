
def separar_pares_impares():
 
    numeros = []
    pares = []
    impares = []

   
    for i in range(20):
        numero = int(input(f"Digite o número {i + 1}: "))
        numeros.append(numero)
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

 
    print("\nVetor de todos os números:", numeros)
    print("Vetor de números pares:", pares)
    print("Vetor de números ímpares:", impares)


separar_pares_impares()
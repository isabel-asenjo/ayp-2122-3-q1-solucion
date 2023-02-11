def repunit(num):
    if len(set(num)) == 1:
        print("Es repunit")
    else: 
        print("No es repunit")

def suma_cuad(num):
    suma_digitos = 0
    for digito in num:
        suma_digitos += int(digito)

    if suma_digitos**(1/2) % 1 == 0:
        print("La suma de sus dígitos es un número cuadrado")
    else:
        print("La suma de sus dígitos no es un número cuadrado")

def main():
    num = input("Ingrese un número: ")
    repunit(num)
    suma_cuad(num)
main()
def ingresar_infractor(db, infraction, officers):
    nombre = input("Nombre: ").capitalize()
    apellido = input("Apellido: ").capitalize()
    while True:
        try:
            ci = int(input("Cédula: "))
            break
        except:
            print("Cédula inválida.")
    print()
    for infraccion in infraction:
        print(f"{infraccion}. {infraction[infraccion]['name']}")
    
    while True:
        try:
            infraccion = int(input("Infracción: "))
            if infraccion in infraction:
                break
            else:
                raise Exception
        except:
            print("Infracción inválida.")
    print()
    for oficial in officers:
        print(f"{oficial}. {officers[oficial]['name']} {officers[oficial]['lastName']}")
    
    while True:
        try:
            oficial = int(input("Oficial: "))
            if oficial in officers:
                break
            else:
                raise Exception
        except:
            print("Oficial inválido.")
    
    db[len(db)+1] = { "Nombre": nombre, "Apellido": apellido, "Cédula": ci, "Infracción": infraccion, "Oficial": oficial }
    
    print("\nInfractor ingresado con éxito!")

def eliminar_infractor(db, infraction, officers):

    mostrar_multas(db, infraction, officers)

    while True:
        try:
            multa = int(input("Id de la multa: "))
            if multa in db:
                break
            else:
                raise Exception
        except:
            print("Id inválido.")

    db.pop(multa)
    print("\nMulta eliminada con éxito!")


def mostrar_multas(db, infraction, officers):
    for ident, info in db.items():
        print(f"{ident}. {info['Nombre']} {info['Apellido']}")
        print("Cédula: ", info["Cédula"])
        print("Infracción: ", infraction[info["Infracción"]]["name"], f"(${infraction[info['Infracción']]['cost']})")
        print("Oficial: ", officers[info["Oficial"]]["name"], officers[info["Oficial"]]["lastName"])
        print()

def main():
    infraction={
        1:{"name":"Choque", "cost":50},
        2:{"name":"Semáforo", "cost":30},
        3:{"name":"Falta de documentos", "cost":100},
    }

    officers={
        1:{"name":"Luis", "lastName":"Bello","ci":13452224},
        2:{"name":"Jose", "lastName":"Quevedo","ci":44235611},
        3:{"name":"Antonio", "lastName":"Guerra","ci":12345678},
    }

    db={}

    while True:
        print("1. Ingresar infractor\n2. Eliminar infractor\n3. Mostrar multas\n4. Salir")
        option=input("Ingrese una opción: ")

        print()

        if option=="1":
            ingresar_infractor(db, infraction, officers)

        elif option=="2":
            eliminar_infractor(db, infraction, officers)

        elif option=="3":
            mostrar_multas(db, infraction, officers)
        
        elif option=="4":
            break

        else:
            print("Opción inválida.")
        
        print()

main()
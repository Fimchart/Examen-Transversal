from Funciones import menu,stock_marca,búsqueda_precio,actualizar_precio

while True:
    menu()
    try:
        opc = int(input("Ingrese una opción: "))
    except ValueError:
        print("\nSolo se permiten numeros.")
        continue

    if opc == 1:
        marca = input("\nIngrese la marca a buscar: ")
        stock_marca(marca)
    elif opc == 2:
        while True:
            try:
                p_min = int(input("Ingrese el precio minimo: "))
                p_max = int(input("Ingrese el precio maximo: "))
                búsqueda_precio(p_min,p_max)
                break
            except ValueError:
                print("Debe ingresar valores enteros.")
                continue
    elif opc == 3:
        while True:
            modelo = input("Ingrese el modelo: ")
            try:
                p = int(input("Ingrese el nuevo precio: "))
                if actualizar_precio(modelo,p):
                    print("\Precio actualizado!")
                else:
                    print("\nEl modelo no existe.")
            except ValueError:
                print("\nIngrese una cantidad valida.")
                continue
            repetir = input("\nDesea actualizar otro precio (si/no)?: ").lower()
            if repetir != "si":
                break
    elif opc == 4:
        print("\n*********************")
        print("\nFINALIZANDO PROGRAMA")
        print("\n*********************")
        break
    else:
        print("Ingrese un numero valido.")
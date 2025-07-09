productos = {"8475HD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i5", "Nvidia GTX1050"],
             "2175HD": ["lenovo", 14, "4GB", "SSD", "512GB", "Intel Core i5", "Nvidia GTX1050"],
             "JjfFHD": ["Asus", 14, "16GB", "SSD", "256GB", "Intel Core i7", "Nvidia RTX2080Ti"],
             "fgdxFHD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i3", "integrada"],
             "GF75HD": ["Asus", 15.6, "8GB", "DD", "1T", "Intel Core i7", "Nvidia GTX1050"],
             "123FHD": ["lenovo", 14, "6GB", "DD", "1T", "AMD Ryzen 5", "integrada"],
             "342FHD": ["lenovo", 15.6, "8GB", "DD", "1T", "AMD Ryzen 7", "Nvidia GTX1050"],
             "UWU131HD": ["Dell", 15.6, "8GB", "DD", "1T", "AMD Ryzen 3", "Nvidia GTX1050"]
             }

Stock = {"8475HD": [387990,10],
         "2175HD": [327990,4],
         "JjfFHD": [424990,1],
         "fgdxFHD": [664990,21],
         "GF75HD": [749990,2],
         "123FHD": [290890,32],
         "342FHD": [444990,7],
         "UWU131HD": [349990,1]
         }


def menu():
    print("\n****** MENU PRINCIPAL ******")
    print("1. Stock marca")
    print("2. Búsqueda por precio")
    print("3. Actualizar precio")
    print("4. Salir\n")


def stock_marca(marca):
    total = 0
    for id, datos in productos.items():
        if datos[0].lower() == marca.lower():
            total += Stock[id][1]
    print(f"\nEl stock de la marca {marca.capitalize()} es: {total}")



def búsqueda_precio(p_min,p_max):
    lista = []
    for id, datos in productos.items():
        precio = Stock[id][0]
        stock = Stock[id][1]
        if p_min <= precio <= p_max and stock > 0:
            lista.append(f"{datos[0]}--{id}")
    if lista:
        print("\nLos productos ente ese rango de precios son: ", sorted(lista))
    else:
        print("\nNo hay notebooks dentro de ese rango de precios.")


def actualizar_precio(modelo,p):
    if modelo in Stock:
        Stock[modelo][0] == p
        return True
    return False








































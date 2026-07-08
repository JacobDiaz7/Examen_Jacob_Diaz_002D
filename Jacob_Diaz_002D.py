juegos = {
'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True,
'NovaStudio'],
'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False,
'BrightWorks'],
'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True,
'OrionGames'],
'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True,
'VelocityLab'],
'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False,
'GreenSeed'],
'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False,
'IronGate'],
}

inventario = {
'G001': [9990, 7],
'G002': [19990, 0],
'G003': [42990, 3],
'G004': [14990, 5],
'G005': [17990, 9],
'G006': [39990, 2],
}

def stock_plataforma(Plat):
    cont=0
    for a in juegos.items():
        if a==Plat:
            cont

def busqueda_precio(precio_minimo, pre_Macimo):
    juego_en_rango=()
    for i in inventario.items():
        if i()>= precio_minimo and i()>= pre_Macimo:
            print("")
        else:
            juego_en_rango




def actualizar_precio(codeJ, newP):
    for codeJ in inventario.items():
        if {0}:
                while True:
                    try:
                        newP=int(input("Ingrese el nuevo precio del Juego: "))
                        while newP>=0:
                            newP=int(input("El juego no puede tener un valor menor a cero"))
                        break
                    except ValueError:
                        print("ERROR")

def agregar_juego(codigo, titulo, plataf, genero, clasi, multi, edito, precio, stock):
    while True:
        try:
            codigo=input("Ingrese el codigo del juego: ").upper().replace()
            while juegos [codigo] in juegos. items() or codigo== "":
                codigo=input("Ingrese el codigo correspondiente del juego: ")
            titulo=input("Ingrese el titulo del juego: ")
            while titulo=="":
                titulo=input("Ingrese un titulo valido")
            plataf=input("Ingrese la plataforma del juego: ")
            while plataf=="":
                plataf=input("Ingrese un nombre de plataforma valido: ")
            genero=input("Ingrese la plataforma del juego: ")
            while genero=="":
                genero=input("Ingrese un nombre de genero valido: ")
            clasi=input("Ingrese la clasificacion del juego: ")
            while clasi=="":
                clasi=input("Ingrese un nombre de clasificacion del juego valido: ")
            multi=input("Tiene multijugador? (Si o NO)").lower
            while multi != "Si" or multi != "No":
                multi=input("Ingrese correctamente si el juego es multijugador: ")
            if multi=="Si":
                multi=True
            else:
                multi=False
            edito=input("Ingrese la editorial del juego: ")
            while edito=="":
                edito=input("Ingrese un nombre valido para la editorial del juego")
            precio=int(input("Ingrese el precio del juego: "))
            while precio<=0:
                precio=int(input("Solo numeros enteros se puede ingresar: "))
            stock=int(input("Ingrese el stock del juego que va agregar: "))
            while stock<=0:
                stock=int(input("Ingrese solo un numero entero para el stock: "))
            juegos[codigo][titulo, plataf, genero, clasi, multi, edito]
        except ValueError:
            print("ERROR")

def  eliminar_juego(codigo):
    for i in juegos.items():
        if codigo:
            del juegos[codigo]
            del inventario[codigo]
            print("Eliminacion")
        else:
            print("")


def Menu():
    while True:
        try:
            print("========== MENÚ PRINCIPAL ==========")
            print("1.- Stock por plataforma")
            print("2.- Búsqueda de juegos por rango de precio")
            print("3.- Actualizar precio de juego")
            print("4.- Agregar juego")
            print("5.- Eliminar juego")
            print("6.- Salir")
            print("=====================================")
            op=int(input("Seleccione un opcion: "))
            match op:
                case 1:
                    plat=input("Ingrese la plataforma")
                    stock_plataforma(plat)
                case 2:
                    try:
                        precio_minimo=int(input("Ingrese el precio minimo: "))
                        precio_macimo=int(input("ingrese el precio maximo: "))
                        while precio_minimo > precio_macimo:
                            print("El precio minimo no puede ser mayor que el maximo")
                            precio_minimo=int(input("Ingrese el precio minimo: "))
                            precio_macimo=int(input("Ingrese el precio maximo: "))
                        break
                    except ValueError:
                        print("ERROR")
                    busqueda_precio
                case 3:
                    while True:
                        try:
                            newP=int(input("Ingrese el nuevo precio del juego: "))
                            while newP<=0:
                                newP=int(input("El juego debe tener un precio superior "))
                            break
                        except ValueError:
                            print

                    actualizar_precio
                case 4:
                    agregar_juego
                case 5:
                    eliminar_juego
                case 6:
                    print("Programa finalizado")
                case _:
                    print("opcion invalida")
        except ValueError:
            print("ERROR")

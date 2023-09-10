from celda import celda
from lista_celdas import lista_celdas

if __name__=="__main__":
    

    def crear_tablero():
        matriz_colores= lista_celdas()
        ancho = input("-------Ingrese el ancho del tablero: ")
        largo = input("-------Ingrese el largo del tablero: ")
        for fila in range(int(largo)):
            for columna in range(int(ancho)):
                nueva_celda= celda(fila+1,columna+1,""," ")
                matriz_colores.insertar(nueva_celda)
        print("")
        b= True
        while b:
            print("Desea ingresar una pieza?")
            print('1, Si')
            print('2. No')
            opcion = input("Eliga una opcion: ")
            print("")
            if opcion=='1':
                fila_pieza= int(input("Ingrese la fila de la pieza a colocar: "))
                columna_pieza= int(input("Ingrese la columna de la pieza a colocar: "))
                print('-----------------COLORES--------------')
                print('- AZUL')
                print('- ROJO')
                print('- VERDE')
                print('- PURPURA')
                print('- NARANJA')
                color_pieza = input('escriba el color de la pieza en mayuscualas sin tildes: ')
                print("")
                matriz_colores.actualizar_tablero(fila_pieza,columna_pieza,color_pieza)
                print('----------------------------------------------------')
                print('            Tablero Actualizado')
                matriz_colores.recorrer_tabla()
            elif opcion=='2':
                print('----------------------------------------------------')
                print('            Tablero Final')
                matriz_colores.recorrer_tabla()
                print('----------------------')
                print('   Grafica Creada')
                print('----------------------')
                matriz_colores.crear_grafica(int(largo),int(ancho))
                print('----------------------')
                print("SALIENDO")
                print('----------------------')
                b = False
    def menu():
        a = True
        while a:
            print('---------------------------------')
            print('            Menu Inicial')
            print('---------------------------------')
            print('1. Crear Tablero')
            print('2. Mostrar datos del Estudiante')
            print('3. Salir')
            opcion = input("Eliga una opcion: ")
            if opcion=="1":
                print('----------------------')
                print('   Crear Tablero')
                print('----------------------')
                crear_tablero()
                print('')
            elif opcion =="2":
                print('----------------------')
                print('  Datos Estudiante')
                print('----------------------')
                print('202202161')
                print('Juan Pascual Itzep Coguox')
                print('Introduccion a la Programacion y Computacion 2')
                print('Seccion D')
                print('')
            elif opcion =="3":
                print('----------------------')
                print("SALIENDO")
                print('----------------------')
                a = False
            else:
                print('----------------------')
                print("ESTA OPCION NO EXISTE")
                print('----------------------')
                print("")
    menu()
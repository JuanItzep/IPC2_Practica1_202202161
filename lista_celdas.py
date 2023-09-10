from nodo import nodo
import os
class lista_celdas:
    def __init__(self):
        self.primero = None

    def insertar(self, celda):
        nodo_nuevo = nodo(celda=celda)
        if self.primero is None:
            self.primero = nodo_nuevo
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_nuevo
    
    def actualizar_tablero(self, fila, columna, color):
        c = True
        actual = self.primero
        while actual!= None:
            if actual.celda.fila == fila and actual.celda.columna == columna:
                if color == 'AZUL':
                    actual.celda.inicial_color= "A"
                    actual.celda.color = color
                    c=False
                elif color == 'ROJO':
                    actual.celda.inicial_color="R"
                    actual.celda.color = color
                    c=False
                elif color == "VERDE":
                    actual.celda.inicial_color="V"
                    actual.celda.color = color
                    c= False
                elif color == "PURPURA":
                    actual.celda.inicial_color="P"
                    actual.celda.color = color
                    c=False
                elif color == "NARANJA":
                    actual.celda.inicial_color="N"
                    actual.celda.color = color
                    c=False
                else:
                    print('---------------------------')
                    print('El color ingresado:',color,"No existe o no fue ingresado correctamente")
                    print('----------------------')
            actual = actual.siguiente
        if c:
            print('---------------------------')
            print('El valor de la columna o fila no se encuentra entre el tablero')
            print('----------------------')
        
    def recorrer_tabla(self):
        actual = self.primero
        centinela_fila=actual.celda.fila
        texto=""
        while actual!=None:
            if centinela_fila==actual.celda.fila:
                texto +="|"+actual.celda.inicial_color
            else:
                print(texto)
                texto="|"+actual.celda.inicial_color
                centinela_fila=actual.celda.fila
            actual = actual.siguiente
        print(texto)
        print('----------------------------------------------------')
    def recorrer(self):
        acutal = self.primero
        while acutal!=None:
            print(acutal.celda.inicial_color+" ")
            acutal = acutal.siguiente
    
    def crear_grafica(self,filast,columnast):
        imagen =open('bb.dot','w',encoding="UTF-8")
        texto = """digraph G{fontname="Helvetica,Arial,sans-serif"node [fontname="Helvetica,Arial,sans-serif"]edge [fontname="Helvetica,Arial,sans-serif"]"""
        texto+="""start[label=\"COLOREALO GUATEMATEL\"]"""
        texto+="a"+str(0)+"""[label=\""""+str(0)+"""\"]"""
        texto+="""start->a"""+str(0)+""";"""
        for fila in range(filast):
            texto+="a"+str(fila+1)+"""[label=\""""+str(fila+1)+"""\"]"""
            texto+="a"+str(fila)+"""->a"""+str(fila+1)+""";"""
        contador= 1
        for columna in range(columnast):
            texto+=str(columna+1)+"""[label=\""""+str(columna+1)+"""\"]"""
            texto+="""start->"""+str(columna+1)+""";"""
            contador+=1
        actual2 = self.primero
        while actual2 != None:
            if actual2.celda.color == 'AZUL':
                texto+=str(contador)+"""[label=\" \"]"""
                texto+=str(contador-int(columnast))+"""->"""+str(contador)+""";"""
                texto+=str(contador)+"""[fillcolor=\"blue\"style=filled]"""
            elif actual2.celda.color == 'ROJO':
                texto+=str(contador)+"""[label=\" \"]"""
                texto+=str(contador-int(columnast))+"""->"""+str(contador)+""";"""
                texto+=str(contador)+"""[fillcolor=\"red\"style=filled]"""
            elif actual2.celda.color == "VERDE":
                texto+=str(contador)+"""[label=\" \"]"""
                texto+=str(contador-int(columnast))+"""->"""+str(contador)+""";"""
                texto+=str(contador)+"""[fillcolor=\"lightgreen\"style=filled]"""
            elif actual2.celda.color == "PURPURA":
                texto+=str(contador)+"""[label=\" \"]"""
                texto+=str(contador-int(columnast))+"""->"""+str(contador)+""";"""
                texto+=str(contador)+"""[fillcolor=\"purple\"style=filled]"""
            elif actual2.celda.color == "NARANJA":
                texto+=str(contador)+"""[label=\" \"]"""
                texto+=str(contador-int(columnast))+"""->"""+str(contador)+""";"""
                texto+=str(contador)+"""[fillcolor=\"orange\"style=filled]"""
            else:
                texto+=str(contador)+"""[label=\" \"]"""
                texto+=str(contador-int(columnast))+"""->"""+str(contador)+""";"""
            contador+=1
            actual2 = actual2.siguiente
        texto+="""}"""
        imagen.write(texto)
        imagen.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng bb.dot -o Tablero_completado.png')
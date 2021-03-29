import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox
from GeneracionNroRandom.generadores import controlGeneradores



class Generador_Numeros(QMainWindow):
    def __init__(self):
        super() . __init__()
        controlador=None
        num_orden=[]
        Semilla=[]
        num_random=[]
        uic.loadUi("ventanaGenerarNumeros.ui",self)
        self.controlador= controlGeneradores()


        self.cmb_MetodoAleatorio.currentIndexChanged.connect(self.accion_seleccionar_metodo)
        self.btn_limpiar.clicked.connect(self.limpiar_interfaz_generar_numeros)
        self.btn_generarNumeros.clicked.connect(self.accion_generar_numeros)
        self.btn_proxNumero.clicked.connect(self.accion_generar_proximo_numero)
        self.btn_limpiarIntervalos.clicked.connect(self.limpiar_interfaz_prueba_frecuencia)
        self.btn_PruebaChiCuadrado.clicked.connect(self.accion_prueba_ChiCuadrado)

    def accion_prueba_ChiCuadrado(self):
        return 0
    def limpiar_interfaz_prueba_frecuencia(self):
        self.txt_intervalos.clear()

    def accion_generar_proximo_numero(self):
        return 0

    def accion_seleccionar_metodo(self):

        # Activo o desactivo input de constante c dependiendo del metodo elegido
        id_metodo = self.cmb_MetodoAleatorio.itemData(self.cmb_MetodoAleatorio.currentIndex())
        if id_metodo == 0:
            self.txt_semilla.setEnabled(True)
            self.txt_cte_a.setEnabled(True)
            self.txt_cte_c.setEnabled(True)
            self.txt_cte_m.setEnabled(True)
        elif id_metodo == 1:
            self.txt_semilla.setEnabled(True)
            self.txt_cte_a.setEnabled(True)
            self.txt_cte_c.clear()
            self.txt_cte_c.setEnabled(False)
            self.txt_cte_m.setEnabled(True)
        else:
            self.txt_semilla.clear()
            self.txt_semilla.setEnabled(False)
            self.txt_cte_a.clear()
            self.txt_cte_a.setEnabled(False)
            self.txt_cte_c.clear()
            self.txt_cte_c.setEnabled(False)
            self.txt_cte_m.clear()
            self.txt_cte_m.setEnabled(False)

    def validar_txt(self):
        return 0

    def accion_generar_numeros(self):

        # Obtengo metodo
        id_metodo = self.cmb_MetodoAleatorio.itemData(self.cmb_MetodoAleatorio.currentIndex())
        s = None
        a = None
        c = None
        m = None
        cantidad_numeros = self.txt_cantNumeros.text()
        if cantidad_numeros == "" or int(cantidad_numeros) <= 0:
            self.mostrar_mensaje("Error", "La cantidad de números tiene que ser mayor a cero")
            return
        # Genero numeros aleatorios dependiendo del metodo seleccionado
        if id_metodo == 0:
            self.nro_orden,self.Semilla, self.num_random = self.controlador.generarNrosAleatoriosMetodoCongruencialMixto(
                s, m, a, c, cantidad_numeros)
        elif id_metodo == 1:
            self.nro_orden, self.Semilla, self.num_random = self.controlador.generarNrosAleatoriosMetodoCongruencialLineal(
                s, m, a, cantidad_numeros)

        elif id_metodo == 2:
            self.num_random = self.controlador.generarMetodoProvistoPorElLenguaje(cantidad_numeros)

        # Cargo tabla
        self.cargar_tabla_numeros_aleatorios(self)

    def cargar_tabla_numeros_aleatorios(self):
        return 0



    def preparar_interfaz(self):
        # Cargo combo box
        self.cmb_MetodoAleatorio.clear()
        self.cmb_MetodoAleatorio.addItem("Método congruencial mixto", 0)
        self.cmb_MetodoAleatorio.addItem("Método congruencial multiplicativo", 1)
        self.cmb_MetodoAleatorio.addItem("Método provisto por el lenguaje", 2)

       # Preparo tabla de numeros generados
        self.dgv_numerosAleatorios.setColumnCount(3)
        self.dgv_numerosAleatorios.setHorizontalHeaderLabels(["Iteracion", "Semilla", "Num random"])

    def limpiar_interfaz_generar_numeros(self):
        # Limpio txts
        self.txt_semilla.clear()
        self.txt_cte_a.clear()
        self.txt_cte_c.clear()
        self.txt_cte_m.clear()
        self.txt_cantNumeros.clear()

        # Selecciono opcion por defecto en combo boxs
        self.cmb_MetodoAleatorio.setCurrentIndex(0)

        # Limpio grilla
        self.dgv_numerosAleatorios.clearSelection()
        self.dgv_numerosAleatorios.setCurrentCell(-1, -1)
        self.dgv_numerosAleatorios.setRowCount(0)

    def mostrar_mensaje(self, titulo, mensaje):
        # Muestro mensaje
        box = QMessageBox()
        box.setWindowTitle(titulo)
        box.setText(mensaje)
        box.setStandardButtons(QMessageBox.Ok)
        box.exec_()

    def showEvent(self, QShowEvent):
        self.preparar_interfaz()
        self.limpiar_interfaz_generar_numeros()
        self.limpiar_interfaz_prueba_frecuencia()

def main():
    app= QApplication(sys.argv)
    GUI= Generador_Numeros()
    GUI.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
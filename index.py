#Projeto de Desenvolvimewnto de uma Calculadora 
#Autor: Gilvan Hilderio da Silva Filho
#Aluno do Curso de Engenharia da Computação
#Faculdade UNINTER

from ast import Lambda
from cgitb import text
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from Calculadora import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        lista = []
        class status: status = True
        def calculadora(arg):

            if arg == 'Limpar':
                self.visor.display('0')
                lista.clear()
            

            elif arg in '0123456789':
                valor = str(self.visor.intValue())
                if len(lista) and lista[-1] == '.': valor += '.'
                if str(self.visor.intValue()) != '0' and status.status == True:
                    self.visor.display(valor + arg)
                else:
                    self.visor.display(str(arg))
                lista.append(arg)
                status.status = True
            elif arg in '+-*/' and ((all(map(lambda x: lista.count(x) <= 1, ['+', '-', '*', '/'])) and len(lista) and '+-*/')):
                status.status = False
                if len(lista) and '+-*/' in lista[-1]: del lista[-1]
                lista.append(arg)

            else:
                if len(lista):
                    print(lista)
                    status.status = False
                    self.visor.display(str(eval(''.join(lista).strip('+-*/'))))
                    lista.clear()
                    resultado = str(self.visor.value())
                    if resultado.endswith('.0'): resultado = resultado.rsplit('.0', 1)[0]
                    lista.append(resultado)
                    if arg != '=': lista.append(arg)

         


        self.b0.clicked.connect(lambda: calculadora(self.b0.text()))
        self.b1.clicked.connect(lambda: calculadora(self.b1.text()))
        self.b2.clicked.connect(lambda: calculadora(self.b2.text()))
        self.b3.clicked.connect(lambda: calculadora(self.b3.text()))
        self.b4.clicked.connect(lambda: calculadora(self.b4.text()))
        self.b5.clicked.connect(lambda: calculadora(self.b5.text()))
        self.b6.clicked.connect(lambda: calculadora(self.b6.text()))
        self.b7.clicked.connect(lambda: calculadora(self.b7.text()))
        self.b8.clicked.connect(lambda: calculadora(self.b8.text()))
        self.b9.clicked.connect(lambda: calculadora(self.b9.text()))
        self.b_Dividir.clicked.connect(lambda: calculadora(self.b_Dividir.text()))
        self.b_Igual.clicked.connect(lambda: calculadora(self.b_Igual.text()))
        self.b_Somar.clicked.connect(lambda: calculadora(self.b_Somar.text()))
        self.b_Multiplicar.clicked.connect(lambda: calculadora(self.b_Multiplicar.text()))
        self.b_Subtrair.clicked.connect(lambda: calculadora(self.b_Subtrair.text()))
        self.b_Ponto.clicked.connect(lambda: calculadora(self.b_Ponto.text()))
        self.b_Limpar.clicked.connect(lambda: calculadora(self.b_Limpar.text()))
        #self.centralWidget#on.addPixmap(QtGui.QPixmap(":/img/gato.ico"), QtGui.QIcon.Mode.Disabled, QtGui.QIcon.State.On)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
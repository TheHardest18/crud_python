from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys
import conexion

def validarCampos():
    if ventana.txtNombre.text() == "" or ventana.txtGmail.text() == "":
        alerta = QMessageBox()
        alerta.setText('Campos no pueden estar vacios!!!')
        alerta.setIcon(QMessageBox.Information)
        alerta.exec()
        return True
def agregar():
    if validarCampos():
        return False
    nombre = ventana.txtNombre.text()
    gmail = ventana.txtGmail.text()

    objContactos = conexion.contactos()
    contactos = objContactos.crearContactos((nombre,gmail))
    consultar()

def modificar():
    if validarCampos():
        return False
    print("Haz sido modificado satisfactoriamente.")
    id = ventana.txtID.text()
    nombre = ventana.txtNombre.text()
    gmail = ventana.txtGmail.text()

    objContactos = conexion.contactos()
    contactos = objContactos.modificarContactos((nombre, gmail, id))
    consultar()
def eliminar():
    print("Haz sido eliminado satisfactoriamente.")
    id = ventana.txtID.text()
    objContactos = conexion.contactos()
    contactos = objContactos.borrarContactos(id)
    consultar()

def cancelar():
    print("Haz sido cancelado satisfactoriamente.")
    consultar()

def consultar():
    ventana.tblDatos.setRowCount(0)
    indiceControl = 0

    objContactos = conexion.contactos()
    contactos = objContactos.leerContactos()
    for contacto in contactos:
        ventana.tblDatos.setRowCount(indiceControl+1)
        ventana.tblDatos.setItem(indiceControl,0, QTableWidgetItem(str(contacto[0])))
        ventana.tblDatos.setItem(indiceControl,1, QTableWidgetItem(str(contacto[1])))
        ventana.tblDatos.setItem(indiceControl,2, QTableWidgetItem(str(contacto[2])))
        indiceControl+=1
    # Espacios en blanco
    ventana.txtID.setText("")
    ventana.txtGmail.setText("")
    ventana.txtNombre.setText("")
    # Desactivar Botones
    ventana.btnAgregar.setEnabled(True)
    ventana.btnEliminar.setEnabled(False)
    ventana.btnModificar.setEnabled(False)
    ventana.btnCancelar.setEnabled(False)
def seleccionar():
    id = ventana.tblDatos.selectedIndexes()[0].data()
    nombre = ventana.tblDatos.selectedIndexes()[1].data()
    gmail = ventana.tblDatos.selectedIndexes()[2].data()
    print(id,nombre,gmail)
    ventana.txtID.setText(id)
    ventana.txtNombre.setText(nombre)
    ventana.txtGmail.setText(gmail)

    ventana.btnAgregar.setEnabled(False)
    ventana.btnEliminar.setEnabled(True)
    ventana.btnModificar.setEnabled(True)
    ventana.btnCancelar.setEnabled(True)

aplicacion = QtWidgets.QApplication([])
ventana = uic.loadUi("ventana.ui")
ventana.show()
consultar()
ventana.tblDatos.cellClicked.connect(seleccionar)
# Dar nombre a las columnas de la tabla Nombre de las columnas
ventana.tblDatos.setHorizontalHeaderLabels(['ID','Nombre', 'Correo '])
# Poner no editable los datos de las columnas
ventana.tblDatos.setEditTriggers(QTableWidget.NoEditTriggers)
# Seleccionar la fila completa.
ventana.tblDatos.setSelectionBehavior(QTableWidget.SelectRows)
ventana.btnAgregar.clicked.connect(agregar)
ventana.btnModificar.clicked.connect(modificar)
ventana.btnEliminar.clicked.connect(eliminar)
ventana.btnCancelar.clicked.connect(cancelar)
sys.exit(aplicacion.exec())

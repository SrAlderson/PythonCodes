#librerias

from tkinter import*
from tkinter import messagebox

#----------------------------------------------------------------------------------------------------------------------
# Base

base = Tk()

#Configuracion - Base
base.title("Expresiones Regurales")
base.resizable (0,0)

#----------------------------------------------------------------------------------------------------------------------
#Funciones

def continuarBoton(op):

    if op == 1:
        #Inicia la ventana para la validacion
        frameProceso()


def frameProceso():

    #Funcion de salida
    def confirmarSalir():

        opcion = messagebox.askokcancel("Expresiones Regulares | Salir ", "¿Desea salir del programa?")
        if opcion == 1:
            baseProceso.destroy()
    
    #Funciones para los cuadros de texto

    def codigoValidar(numero):

        match numero: 
            case 1:
                mensaje = cuadroTexto1.get () # Esto recibe el texto de la caja de texto
                #Aqui irian las validaciones por ER
                messagebox.showinfo("Expresiones Regulares | Validacion","La cadena: " + mensaje + "Poner aqui el tipo de ER")
            case 2:
                mensaje = cuadroTexto1.get () # Esto recibe el texto de la caja de texto
                #Aqui irian las validaciones por ER
                messagebox.showinfo("Expresiones Regulares | Validacion","La cadena: " + mensaje + "Poner aqui el tipo de ER")
            case 3:
                mensaje = cuadroTexto1.get () # Esto recibe el texto de la caja de texto
                #Aqui irian las validaciones por ER
                messagebox.showinfo("Expresiones Regulares | Validacion","La cadena: " + mensaje + "Poner aqui el tipo de ER")
            case 4: 
                mensaje = cuadroTexto1.get () # Esto recibe el texto de la caja de texto
                #Aqui irian las validaciones por ER
                messagebox.showinfo("Expresiones Regulares | Validacion","La cadena: " + mensaje + "Poner aqui el tipo de ER")

    # Se elimina la ventana de inicio
    base.destroy()

    baseProceso = Tk()
    #Configuracion - Base
    baseProceso.title("Expresiones Regurales")
    baseProceso.resizable (0,0)

    # Frame
    miFrame = Frame(baseProceso)
    miFrame.pack(fill= "both",expand="TRUE")

    # Widget 

    #Label del titulo principal
    labelTitulo = Label(miFrame, text="Categorizacion de cadenas con ER" , font=("Consolas", 18))
    labelTitulo.grid(row=0 , column=1, padx= 10, pady = 10, columnspan=4)

    #Label de cadena1 
    labelCadena1 = Label(miFrame, text="Cadena 1: ")
    labelCadena1.grid(row= 2, column=2, padx= 20, pady = 10)
    labelCadena1.config(font=("Consolas", 12))

    #Label de cadena2 
    labelCadena2 = Label(miFrame, text="Cadena 2: ")
    labelCadena2.grid(row=3, column=2, padx= 20, pady = 10)
    labelCadena2.config(font=("Consolas", 12))

    #Label de cadena3
    labelCadena3 = Label(miFrame, text="Cadena 3: ")
    labelCadena3.grid(row=4 , column=2, padx= 20, pady = 10)
    labelCadena3.config(font=("Consolas", 12))

    #Label de cadena4 
    labelCadena4 = Label(miFrame, text="Cadena 4: ")
    labelCadena4.grid(row = 5, column=2, padx= 20, pady = 10)
    labelCadena4.config(font=("Consolas", 12))

    #Cuadro de texto cadena1
    cuadroTexto1 = Entry(miFrame)
    cuadroTexto1.grid(row=2, column=3, padx= 5, pady = 10)
    cuadroTexto1.config(font=("Consolas", 12))

    #Cuadro de texto cadena2
    cuadroTexto2 = Entry(miFrame)
    cuadroTexto2.grid(row=3, column=3, padx= 5, pady = 10)
    cuadroTexto2.config(font=("Consolas", 12))

    #Cuadro de texto cadena3
    cuadroTexto3 = Entry(miFrame)
    cuadroTexto3.grid(row=4, column=3, padx= 5, pady = 10)
    cuadroTexto3.config(font=("Consolas", 12))

    #Cuadro de texto cadena4
    cuadroTexto4 = Entry(miFrame)
    cuadroTexto4.grid(row=5, column=3, padx= 5, pady = 10)
    cuadroTexto4.config(font=("Consolas", 12))

    #Boton Validar Cadena 1
    botonValidarC1 = Button (miFrame, text= "Validar", cursor="hand2" , command = lambda:codigoValidar(1))
    botonValidarC1.grid(row=2, column= 4, padx= 20, pady = 10)

    #Boton Validar Cadena 2
    botonValidarC2 = Button (miFrame, text= "Validar", cursor="hand2" , command = lambda:codigoValidar(2))
    botonValidarC2.grid(row=3, column= 4, padx= 20, pady = 10)

    #Boton Validar Cadena 3
    botonValidarC3 = Button (miFrame, text= "Validar", cursor="hand2" , command = lambda:codigoValidar(3))
    botonValidarC3.grid(row=4, column= 4, padx= 20, pady = 10)

    #Boton Validar Cadena 4
    botonValidarC4 = Button (miFrame, text= "Validar", cursor="hand2" , command = lambda:codigoValidar(4))
    botonValidarC4.grid(row=5, column= 4, padx= 20, pady = 10)

    #Boton Salir
    botonSalir = Button (miFrame, text="Salir", cursor="hand2" , command = lambda:confirmarSalir())
    botonSalir.grid (row=7 , column= 3, padx=20 , pady=10)

#----------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------
# Frame | Ventana de inicio

miFrameInicial = Frame(base)
miFrameInicial.pack(fill= "both",expand="TRUE")

#Label del titulo principal
labelTitulo = Label(miFrameInicial, text="Categorización de cadenas con ER" , font=("Concert One", 18))
labelTitulo.grid(row=0 , column=1, padx= 10, pady = 10, columnspan=4)

#Logo
imagenInicio = PhotoImage(file="logo.png")
labaelImagenInicio = Label(miFrameInicial, image=imagenInicio)
labaelImagenInicio.grid(row=2, column=1, padx=10, pady=10, columnspan=4)

#Label titulo integrantes
labelT1 = Label(miFrameInicial, text="Integrantes" , font=("Consolas", 18))
labelT1.grid(row=4 , column=1, padx= 10, pady = 10, columnspan=4)

#Label integrante 1
labelIntegrante1 = Label(miFrameInicial, text="Andres Castro" , font=("Consolas", 18))
labelIntegrante1.grid(row=5 , column=1, padx= 10, pady = 10, columnspan=4)

#Label integrante 2
labelIntegrante1 = Label(miFrameInicial, text="Jessica Cedeño" , font=("Consolas", 18))
labelIntegrante1.grid(row=6 , column=1, padx= 10, pady = 10, columnspan=4)

#Label integrante 3
labelIntegrante1 = Label(miFrameInicial, text="Giovanni Gonzalez" , font=("Consolas", 18))
labelIntegrante1.grid(row=7 , column=1, padx= 10, pady = 10, columnspan=4)

#Botones

#Boton Continuar
botonSalir = Button (miFrameInicial, text="Continuar", cursor="hand2" ,command = lambda:frameProceso())
botonSalir.grid (row=9 , column= 1, padx=20 , pady=10, columnspan=4)

#----------------------------------------------------------------------------------------------------------------------

# Linea de ejecucion
base.mainloop()

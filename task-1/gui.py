from cProfile import label
from tkinter import *
import tkinter
import coordinator

from setuptools import Command

root = tkinter.Tk()
root.geometry('400x300')

error = StringVar()
solution = StringVar()


def getContent():
    min_num = int(entry1.get())
    max_num = int(entry2.get())
    
    if(min_num >= max_num):
        print('Error')
        error.set("Ingrese un valor minimo inferior al maximo")
        solution.set("")
        
    else:
        value = coordinator.ejecutar_todos_los_calculos(min_num, max_num)
        print(value)
        #solution.set(f"Su resultado es:{min + max}")
        print(min_num,max_num)

labeTitle = Label(root, width=50 , text="Suma de Intervalo , de forma paralela")
labeTitle.pack()
label = Label(root, width=20 , text="Valor minimo del Intervalo")
label.pack()
entry1 = Entry(root, width = 20)
entry1.pack()

label2 = Label(root, width=20 , text="Valor maximo del Intervalo")
label2.pack()
entry2 = Entry(root, width = 20)
entry2.pack()

label3 = Label(root, width=50 , textvariable=error  )
label3.pack()

labelResultado = Label(root, width=50 , textvariable= solution )
labelResultado.pack()


Button(root,text="Enviar",command= getContent).pack()
root.mainloop()
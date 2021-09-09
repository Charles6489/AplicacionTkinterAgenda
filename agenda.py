from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

ventana = Tk()
ventana.title("App")
ventana.geometry("400x400")
ventana.resizable(0,0)
ventana.config(bg="#e0f70f")
colorfondo="#e0f70f"
titulo = Label(ventana,text="Registro de usuarios",bg=colorfondo,font=('Helvetica',15))
titulo.place(x=100,y=0)



def cargar():
    listbox.insert(listbox.size(), nombre.get() +" "+ apellido.get() + " "+ telefono.get())
    nombre.set("")
    apellido.set("")
    telefono.set("")
    listbox.configure(height=listbox.size())


def eliminar():    
    if (messagebox.askquestion(title="Eliminar Usuario",message="Esta seguro de elimiar el usuario")):
        for index in reversed(listbox.curselection()):
            listbox.delete(index)
    listbox.configure(height=listbox.size())



def guardar():
    file = filedialog.asksaveasfile(initialdir="D:\\VCS\\python\\python_tkinter",defaultextension=".txt",filetypes=[("Text File",".txt"),("Text html",".html"),("Text html",".*")])
    filetext = str(listbox.get(0,END))
    file.write(filetext)
    file.close()



nombre = StringVar()
apellido = StringVar()
telefono = StringVar()
mostrar = StringVar()
etiquetanombre = Label(ventana,text="Nombre : ",bg=colorfondo).place(x=50,y=40)
etiquetanombre = Label(ventana,text="Apellido : ",bg=colorfondo).place(x=50,y=80)
etiquetanombre = Label(ventana,text="Telefono : ",bg=colorfondo).place(x=50,y=120)


#mostrar1 = Entry(ventana,state="disable",textvariable=mostrar,width=50).place(x=0,y=300)

entradanombre = Entry(ventana,textvariable=nombre,border=10).place(x = 150,y=40)
entradaapellido = Entry(ventana,textvariable=apellido,border=10).place(x = 150,y=80)
entradatelefono = Entry(ventana,textvariable=telefono,border=10).place(x = 150,y=120)

boton1 =Button(ventana,text="Cargar",command=cargar,border=5).place(x=80,y=180)
boton2 = Button(ventana,text="Eliminar",command=eliminar,border=5).place(x=150,y=180)
boton3 = Button(ventana,text="Guardar",border=5,command=guardar).place(x=230,y=180)


listbox = Listbox(ventana, 
                    bg="white",
                    font=('Arial',10),
                    width=50,
                    height=80,
                    selectmode=MULTIPLE)
label1  = Label(ventana,text="Lista de Usuarios",bg=colorfondo).place(x=150,y=220)

listbox.place(x=20,y=250)
listbox.configure(height=listbox.size())

ventana.mainloop()

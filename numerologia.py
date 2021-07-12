from calculo_numerologia import numerologia, numerologia_nombre
from validador import validar_fecha

from tkinter import (
    Tk,
    Frame,
    Label,
    Entry,
    Button,
    StringVar,
    PhotoImage,
    messagebox,
)

from tkinter.constants import (
    SOLID,
    N,
    S,
    E,
    W,
    X,
    Y,
    FLAT,
    RAISED,
    TRUE,
    FALSE,
    CENTER,
    TOP,
    BOTTOM,
    LEFT,
    BOTH,
    NO,
    YES,
    NSEW,
    END,
)


class VistaFecha:
    def __init__(self, root=None):
        self.root = root
        # self.root.iconbitmap("om.ico")
        # self.root.tittle("Numerologia")
        self.root.resizable(0, 1)

        ###############
        self.var_dia = StringVar()
        self.var_mes = StringVar()
        self.var_anio = StringVar()
        self.var_nombre = StringVar()
        self.var_apellido = StringVar()
        self.var_iniciales = StringVar()
        #### Estetico
        # FRAMES #########
        self.fr_fecha = Frame(self.root, background="#fff")
        self.fr_bttn = Frame(self.root, background="#fff")
        self.fr_nombre = Frame(self.root, background="#fff")
        self.fr_iniciales = Frame(self.root, background="#fff")
        # LABELS #######
        self.lb_fecha = Label(
            self.fr_fecha,
            text="Ingrese una fecha",
            background="#b8b8b8",
            justify=CENTER,
        )
        self.lb_dia = Label(
            self.fr_fecha,
            text="DIA --> DD",
            background="#b8b8b8",
            justify=CENTER,
        )

        self.lb_mes = Label(
            self.fr_fecha,
            text="mes --> MM",
            background="#b8b8b8",
            justify=CENTER,
        )

        self.lb_anio = Label(
            self.fr_fecha,
            text="AÑO --> AAAA",
            background="#b8b8b8",
            justify=CENTER,
        )
        self.lb_nombre = Label(
            self.fr_nombre,
            text="Nombre Completo",
            background="#b8b8b8",
            justify=CENTER,
        )
        self.lb_apellido = Label(
            self.fr_nombre,
            text="Apellido Completo",
            background="#b8b8b8",
            justify=CENTER,
        )
        self.lb_iniciales = Label(
            self.fr_iniciales,
            text="Introduce Iniciales, Texto y/o Numeros(letras / iniciales / DNI)",
            background="#b8b8b8",
            justify=CENTER,
        )
        # Entry ##############
        self.en_dia = Entry(
            self.fr_fecha,
            textvariable=self.var_dia,
            width=40,
            relief=SOLID,
            justify=CENTER,
        )
        self.en_mes = Entry(
            self.fr_fecha,
            textvariable=self.var_mes,
            width=40,
            relief=SOLID,
            highlightbackground="DarkOrchid3",
            highlightcolor="DarkOrchid3",
            justify=CENTER,
        )
        self.en_anio = Entry(
            self.fr_fecha,
            textvariable=self.var_anio,
            width=40,
            relief=SOLID,
            highlightbackground="DarkOrchid3",
            highlightcolor="DarkOrchid3",
            justify=CENTER,
        )
        self.en_nombre = Entry(
            self.fr_nombre,
            textvariable=self.var_nombre,
            width=40,
            relief=SOLID,
            justify=CENTER,
        )
        self.en_apellido = Entry(
            self.fr_nombre,
            textvariable=self.var_apellido,
            width=40,
            relief=SOLID,
            justify=CENTER,
        )
        self.en_iniciales = Entry(
            self.fr_iniciales,
            textvariable=self.var_iniciales,
            width=40,
            relief=SOLID,
            justify=CENTER,
        )
        # button ######
        self.bt_Karmico = Button(
            self.fr_bttn,
            text="Num Karmico",
            bg="#b8b8b8",
            justify=CENTER,
            cursor="exchange",
            command=lambda: self.calcula_karma(),
        )
        self.bt_vida_maestro = Button(
            self.fr_bttn,
            text="Num Vida",
            bg="#b8b8b8",
            justify=CENTER,
            cursor="exchange",
            command=lambda: self.calcula_vida_maestro(),
        )
        self.bt_nombre = Button(
            self.fr_bttn,
            text="Nombre",
            bg="#b8b8b8",
            justify=CENTER,
            cursor="exchange",
            command=lambda: self.nombre_apellido(),
        )

        self.bt_iniciales = Button(
            self.fr_bttn,
            text="iniciales",
            bg="#b8b8b8",
            justify=CENTER,
            cursor="exchange",
            command=lambda: self.nombre_iniciales(),
        )
        ######### PACK
        self.fr_fecha.pack(side=TOP, expand=True, fill=BOTH, padx=2, pady=2)
        self.lb_fecha.pack(side=TOP, expand=True, fill=X)
        self.lb_dia.pack(anchor=N + W, side=LEFT, expand=True, fill=X, padx=5, pady=2)
        self.en_dia.pack(anchor=N + W, side=LEFT, expand=True, fill=X, padx=5, pady=2)
        self.lb_mes.pack(anchor=N + W, side=LEFT, expand=True, fill=X, padx=5, pady=2)
        self.en_mes.pack(anchor=N, side=LEFT, expand=True, fill=X, padx=5, pady=2)
        self.lb_anio.pack(anchor=N + W, side=LEFT, expand=True, fill=X, padx=5, pady=2)
        self.en_anio.pack(anchor=N + E, side=LEFT, expand=True, fill=X, padx=5, pady=2)
        self.bt_Karmico.pack(side=LEFT, expand=FALSE, fill=None, padx=10)
        self.bt_vida_maestro.pack(side=LEFT, expand=FALSE, fill=None, padx=10)
        self.bt_nombre.pack(side=LEFT, expand=FALSE, fill=None, padx=10)
        self.fr_nombre.pack(anchor=N, side=TOP, expand=True, fill=X, padx=2, pady=2)
        self.lb_nombre.pack(
            anchor=N + W, side=LEFT, expand=True, fill=X, padx=5, pady=2
        )
        self.en_nombre.pack(
            anchor=N + E, side=LEFT, expand=True, fill=X, padx=5, pady=2
        )
        self.lb_apellido.pack(
            anchor=N + W, side=LEFT, expand=True, fill=X, padx=5, pady=2
        )
        self.en_apellido.pack(
            anchor=N + E, side=LEFT, expand=True, fill=X, padx=5, pady=2
        )
        self.fr_bttn.pack(anchor=N, side=TOP, expand=True, fill=X, padx=2, pady=2)
        self.fr_iniciales.pack(anchor=N, side=TOP, expand=True, fill=X, padx=2, pady=2)
        self.lb_iniciales.pack(
            anchor=N + W, side=TOP, expand=True, fill=X, padx=5, pady=2
        )
        self.en_iniciales.pack(
            anchor=N + E, side=LEFT, expand=True, fill=X, padx=5, pady=2
        )
        self.bt_iniciales.pack(side=LEFT, expand=FALSE, fill=None, padx=10)
        # metodos ###########

    ##########################################################################################
    ##########################################################################################
    ##########################################################################################
    def calcula_karma(self):
        print("Karmico")
        cadena = self.var_dia.get() + self.var_mes.get() + self.var_anio.get()
        try:
            print(int(cadena))

            try:
                self.lb_karma.destroy()
            except:
                pass
            try:
                self.calculadora = numerologia(
                    self.var_dia.get(), self.var_mes.get(), self.var_anio.get()
                )
                self.numero_karmico = self.calculadora.karmico()
                if self.numero_karmico == None:
                    messagebox.showinfo(
                        "Error", "ingrese una fecha valida Dia[DD] Mes[MM] Año[AAAA]"
                    )
                else:
                    self.karma = "numero KARMICO : " + str(self.numero_karmico)
                    self.lb_karma = Label(
                        self.root,
                        text=self.karma,
                        background="#db4035",
                        justify=CENTER,
                    )
                    self.lb_karma.pack(side=BOTTOM, expand=True, fill=X, anchor=S)
            except:
                print("error calcula()")
                raise
        except:
            messagebox.showerror(
                "Error", "ingrese una fecha valida Dia[DD] Mes[MM] Año[AAAA]"
            )

    def calcula_vida_maestro(self):
        print("Numero de Vida")
        cadena = self.var_dia.get() + self.var_mes.get() + self.var_anio.get()
        try:
            print(int(cadena))
            try:
                self.lb_vida.destroy()
            except:
                pass
            try:
                self.calculadora = numerologia(
                    self.var_dia.get(), self.var_mes.get(), self.var_anio.get()
                )
                self.num_vida_maestro = self.calculadora.vida_maestro()
                self.vida = "numero VIDA : " + str(self.num_vida_maestro)
                self.lb_vida = Label(
                    self.root,
                    text=self.vida,
                    background="#f93",
                    justify=CENTER,
                )
                self.lb_vida.pack(side=BOTTOM, expand=True, fill=X, anchor=S)
            except:
                print("error calcula()")
                raise
        except:
            messagebox.showerror(
                "Error de Fecha", "ingrese una fecha valida (DD MM AAAA"
            )

    def nombre_apellido(self):
        try:
            try:
                self.lb_nombre_apello.destroy()
            except:
                pass
            if not self.var_nombre.get() or not self.var_apellido.get():
                messagebox.showinfo(
                    "Error de nombre",
                    "Nombre o Apellido vacio, completa ambos, Gracias",
                )
            else:
                self.cadena = self.var_nombre.get() + " " + self.var_apellido.get()
                calculo_nombre = numerologia_nombre(self.cadena)
                self.resultado_nombre_apellido = calculo_nombre.numero_nombre_completo()
                if (
                    self.resultado_nombre_apellido == None
                    or self.resultado_nombre_apellido == "0"
                ):
                    messagebox.showinfo("Error", "ingrese solo texto")
                else:
                    self.text_nombre_apello = (
                        "Reduccion Numerologica de Nombre y Apellido:",
                        self.resultado_nombre_apellido,
                    )
                    self.lb_nombre_apello = Label(
                        self.root,
                        text=self.text_nombre_apello,
                        background="#fad000",
                        justify=CENTER,
                    )
                    self.lb_nombre_apello.pack(
                        side=BOTTOM, expand=True, fill=X, anchor=S
                    )
        except:
            messagebox.showerror(
                "Error de Nombre Completo", "ingrese un Nombre y Apellido valido"
            )

    def nombre_iniciales(self):
        try:
            try:
                self.lb_nombre_iniciales.destroy()
            except:
                pass
            if not self.var_iniciales.get():
                messagebox.showinfo(
                    "Error de iniciales",
                    "Campo vacio, introduce iniciales o un texto",
                )
            else:
                calculo_nombre = numerologia_nombre(self.var_iniciales.get())
                self.resultado_nombre_iniciales = calculo_nombre.numero_iniciales()
                if self.resultado_nombre_iniciales == None:
                    messagebox.showinfo("Error", "ingrese solo texto")
                else:
                    print(
                        "el resultado de ",
                        self.var_iniciales.get(),
                        "es : ",
                        self.resultado_nombre_iniciales,
                    )
                    self.text_nombre_iniciales = (
                        "Reduccion Numerologica de los Caracteres:",
                        self.resultado_nombre_iniciales,
                    )
                    self.lb_nombre_iniciales = Label(
                        self.root,
                        text=self.text_nombre_iniciales,
                        background="#299438",
                        justify=CENTER,
                    )
                    self.lb_nombre_iniciales.pack(
                        side=BOTTOM, expand=True, fill=X, anchor=S
                    )
        except:
            messagebox.showerror(
                "Error de Caracteres",
                "No se pudo calcular la numerologia de los caracteres",
            )


if __name__ == "__main__":
    ventana = Tk()
    programa = VistaFecha(ventana)
    ventana.mainloop()
    """
    #db4035 red
    #f93 orange
    #fad000 yellow
    #299438 green
    #96c3b light blue 
    #af38eb blue
    #b9b9b9 gris
    """
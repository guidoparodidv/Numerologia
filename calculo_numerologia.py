import re


class numerologia:
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

    def karmico(self):
        try:
            a = (
                int(self.dia[0])
                + int(self.dia[1])
                + int(self.mes[0])
                + int(self.mes[1])
                + int(self.anio[0])
                + int(self.anio[1])
                + int(self.anio[2])
                + int(self.anio[3])
            )
            b = str(a)
            try:
                c = int(b[0]) + int(b[1])
                d = str(c)
                try:
                    e = int(d[0]) + int(d[1])
                    f = str(e)
                    return f
                except:
                    return d
            except:
                return b
        except:
            print("Error", "No se pudo realizar la suma del numero KARMICO")

    def vida_maestro(self):
        try:
            a = (
                int(self.dia[0])
                + int(self.dia[1])
                + int(self.mes[0])
                + int(self.mes[1])
                + int(self.anio[0])
                + int(self.anio[1])
                + int(self.anio[2])
                + int(self.anio[3])
            )
            b = str(a)
            try:
                if b == "11" or b == "22" or b == "33" or b == "44":
                    return b
                else:
                    c = int(b[0]) + int(b[1])
                    d = str(c)
                    try:
                        if d == "11" or d == "22" or d == "33" or d == "44":
                            return d
                        else:
                            e = int(d[0]) + int(d[1])
                            f = str(e)
                            return f
                    except:
                        return d
            except:
                return b
        except:
            print("Error", "No se pudo realizar la suma del numero KARMICO")


class numerologia_nombre:
    def __init__(self, cadena):
        self.str_nombre = cadena
        self.numero_cadena = 0

    def regex_string(self, string):
        self.cadena = string
        print("calculando la numerologia para la/s palabra/s", self.cadena)
        print("cadena", self.cadena)
        for i in self.cadena:
            try:
                if i == " ":
                    print(i, "= +0", self.numero_cadena)
                    continue
                elif (
                    i == "a" or i == "A" or i == "j" or i == "J" or i == "s" or i == "S"
                ):
                    # a =e A = j = J = s = S = 1
                    self.numero_cadena = self.numero_cadena + 1
                    print(i, "= +1", self.numero_cadena)
                    continue
                elif (
                    i == "b" or i == "B" or i == "k" or i == "K" or i == "t" or i == "T"
                ):
                    # b = B = k = K = t = T = 2
                    self.numero_cadena = self.numero_cadena + 2
                    print(i, "= +2", self.numero_cadena)
                    continue
                elif (
                    i == "c" or i == "C" or i == "l" or i == "L" or i == "u" or i == "U"
                ):
                    # c = C = l = L = u = U = 3
                    self.numero_cadena = self.numero_cadena + 3
                    print(i, "= +3", self.numero_cadena)
                    continue
                elif (
                    i == "d" or i == "D" or i == "m" or i == "M" or i == "v" or i == "V"
                ):
                    # d = D = m = M = v = V = 4
                    self.numero_cadena = self.numero_cadena + 4
                    print(i, "= +4", self.numero_cadena)
                    continue
                elif (
                    i == "e"
                    or i == "E"
                    or i == "n"
                    or i == "N"
                    or i == "ñ"
                    or i == "Ñ"
                    or i == "w"
                    or i == "W"
                ):
                    # e = E = n = N = ñ = Ñ = w = W = 5
                    self.numero_cadena = self.numero_cadena + 5
                    print(i, "= +5", self.numero_cadena)
                    continue
                elif (
                    i == "f" or i == "F" or i == "o" or i == "O" or i == "x" or i == "X"
                ):
                    # f = F = o = O = x = X = 6
                    self.numero_cadena = self.numero_cadena + 6
                    print(i, "= +6", self.numero_cadena)
                    continue
                elif (
                    i == "g" or i == "G" or i == "p" or i == "P" or i == "y" or i == "Y"
                ):
                    # g = G = p = P = y = Y = 7
                    self.numero_cadena = self.numero_cadena + 7
                    print(i, "= +7", self.numero_cadena)
                    continue
                elif (
                    i == "h" or i == "H" or i == "q" or i == "Q" or i == "z" or i == "Z"
                ):
                    # h = H = q = Q = z = Z = 8
                    self.numero_cadena = self.numero_cadena + 8
                    print(i, "= +8", self.numero_cadena)
                    continue
                elif i == "i" or i == "I" or i == "r" or i == "R":
                    # i = I = r = R = 9
                    self.numero_cadena = self.numero_cadena + 9
                    print(i, "= +9", self.numero_cadena)
                    continue
                ################ NUMEROS
                elif i == "1":
                    self.numero_cadena = self.numero_cadena + 1
                    print(i, "= +1", self.numero_cadena)
                    continue
                elif i == "2":
                    self.numero_cadena = self.numero_cadena + 2
                    print(i, "= +2", self.numero_cadena)
                    continue
                elif i == "3":
                    self.numero_cadena = self.numero_cadena + 3
                    print(i, "= +3", self.numero_cadena)
                    continue
                elif i == "4":
                    self.numero_cadena = self.numero_cadena + 4
                    print(i, "= +4", self.numero_cadena)
                    continue
                elif i == "5":
                    self.numero_cadena = self.numero_cadena + 5
                    print(i, "= +5", self.numero_cadena)
                    continue
                elif i == "6":
                    self.numero_cadena = self.numero_cadena + 6
                    print(i, "= +6", self.numero_cadena)
                    continue
                elif i == "7":
                    self.numero_cadena = self.numero_cadena + 7
                    print(i, "= +7", self.numero_cadena)
                    continue
                elif i == "8":
                    self.numero_cadena = self.numero_cadena + 8
                    print(i, "= +8", self.numero_cadena)
                    continue
                elif i == "9":
                    self.numero_cadena = self.numero_cadena + 9
                    print(i, "= +9", self.numero_cadena)
                    continue

                ################## caracteres que no son ni numeros ni letras
                else:
                    print(i, "= +0", self.numero_cadena)
                    continue
            except:
                print("########################")
                print("error con la cadena", self.cadena)
                print("########################")
        print("numero nombre", self.numero_cadena)
        cadena_inicial = str(self.numero_cadena)
        try:
            print("intenta reducir")
            try:
                print("Reduccion 1")
                self.primer_reduccion = (
                    int(cadena_inicial[0])
                    + int(cadena_inicial[1])
                    + int(cadena_inicial[2])
                )
                print("Primer reduccion", self.primer_reduccion)
                try:
                    print("Reduccion 2")
                    segunda_cadena = str(self.primer_reduccion)
                    self.segunda_reduccion = int(segunda_cadena[0]) + int(
                        segunda_cadena[1]
                    )
                    print("Segunda recuccion", self.segunda_reduccion)
                    try:
                        print("Reduccion 3")
                        tercer_cadena = str(self.segunda_reduccion)
                        self.tercer_recuccion = int(tercer_cadena[0]) + int(
                            tercer_cadena[1]
                        )
                        print("tercer reduccion", self.tercer_recuccion)
                        return str(self.tercer_recuccion)
                    except:
                        return str(self.segunda_reduccion)
                except:
                    return str(self.primer_reduccion)
            except:
                print("no tiene 3 digitos, vamos a reducir los 2 digitos")
                print("Reduccion 1")
                self.primer_reduccion = int(cadena_inicial[0]) + int(cadena_inicial[1])
                print("Primer reduccion", self.primer_reduccion)
                try:
                    print("Reduccion 2")
                    segunda_cadena = str(self.primer_reduccion)
                    self.segunda_reduccion = int(segunda_cadena[0]) + int(
                        segunda_cadena[1]
                    )
                    print("Segunda recuccion", self.segunda_reduccion)
                    return str(self.segunda_reduccion)
                except:
                    return str(self.primer_reduccion)
        except:
            print("no se pudo reducir")
            return str(self.numero_cadena)

    def numero_nombre_completo(self):
        self.cadena = self.str_nombre
        resultado = self.regex_string(self.cadena)
        return resultado

    def numero_iniciales(self):
        self.cadena = self.str_nombre
        resultado = self.regex_string(self.cadena)
        return resultado


if __name__ == "__main__":
    print(__name__)
    # ###################
    # backend = numerologia("28", "02", "1979")
    # print(backend.karmico())
    # print(backend.vida_maestro())
    # ###################
    # parametro = ""
    # a = "guido ignacio gorosito parodi"
    # b = "Zoe"
    # c = "Alejandra"
    # nombre = numerologia_nombre(b, parametro)
    # print(nombre.numero_nombre_completo())

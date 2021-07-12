import re
from re import match


def validar_fecha(cad_validar):
    patron = "[0-9][0-9999]"
    print("comparando la cadena (cad_val):", cad_validar, ", con el patron:", patron)
    try:
        if re.match(patron, cad_validar):
            return "True"
        else:
            return "False"
    except:
        print("Except")
        return "False"


if __name__ == "__main__":
    print("########### TRUE ################")
    print(validar_fecha("28021979"))
    print(validar_fecha("21112013"))
    print(validar_fecha("29051990"))
    print(validar_fecha("99999999"))
    print(validar_fecha("00000000"))
    print("########### FALSE ################")
    print(validar_fecha("9999999a"))
    print(validar_fecha("999999a9"))
    print(validar_fecha("99999a99"))
    print(validar_fecha("9999a999"))
    print(validar_fecha("999a9999"))
    print(validar_fecha("99a99999"))
    print(validar_fecha("9a999999"))
    print(validar_fecha("a9999999"))
    print(validar_fecha("aaaaaaaa"))
    print(validar_fecha("9aaaaaaa"))
    print(validar_fecha("99aaaaaa"))
    print("##########################")
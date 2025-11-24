apertura="(, {, [,"
cierre="), }, ],"
signos="-+*/^"
while True:
    print("ingrsa la oppcion que deceea realizar:")
    print("1.verificar ecuacion")
    print("2.salir")
    oppcion=input()
    if oppcion=="1":
        ecuacion=input("ingresa la ecuacion:")
        pila=[]
        for char in ecuacion:
            if char in apertura:
                pila.append(char)
            elif char in cierre:
                if len(pila)==0:
                    print("la ecuacion no esta balanceada")
                    break
                else:
                    tope=pila.pop()
                    if apertura.index(tope)!=cierre.index(char):
                        print("la ecuacion no esta balanceada")
                        break
        else:
            if len(pila)==0:
                print("la ecuacion esta balanceada")
            else:
                print("la ecuacion no esta balanceada")
    elif oppcion=="2":
        print("saliendo del programa")
        break
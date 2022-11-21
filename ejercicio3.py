print("¿Riman las palabras?\n")

respuesta = "s"

while respuesta.lower().__eq__("s"):
    print("Introduzca una palabra")
    palabra1 = input()
    print("Introduzca otra palabra")
    palabra2 = input()

    if palabra1[-3:].lower().__eq__(palabra2[-3:].lower()):
        print(f"Las palabras {palabra1} y {palabra2} si riman.")
    else:
        if palabra1[-2:].lower().__eq__(palabra2[-2:].lower()):
            print(f"Las palabras {palabra1} y {palabra2} riman un poco.")
        else:
            print(f"Las palabras {palabra1} y {palabra2} no riman")

    print("¿Desea volver a jugar? (s/n)")
    respuesta = input()

    while not respuesta.lower().__eq__("s") and not respuesta.lower().__eq__("n"):
        print("La respuesta no es correcta")

        print("¿Desea volver a jugar? (s/n)")
        respuesta = input()
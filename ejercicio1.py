print("El reino del dragón\n")

import random

cont = 0
explora = "p"
salir = False
puntos = 0
respuesta = "s"

while respuesta.lower().__eq__("s"):
    while cont < 5 and not salir:
        cuevaMala = round(random.random())
        print(cuevaMala)

        print("Quiere ir a la cueva (a/b)")
        explora = input()

        while not explora.lower().__eq__("a") and not explora.lower().__eq__("b"):
            print("La respuesta no es correcta")

            print("Quiere ir a la cueva (a/b)")
            explora = input()

        if cuevaMala == 0 and explora.lower().__eq__("a"):
            salir = True
        else:
            if cuevaMala == 1 and explora.lower().__eq__("b"):
                salir = True
            else:
                puntos += 100

        if not salir:
            print("Te has encontrado un dragón amable y te ha cedido su tesoro, has obtenido 100 puntos.")
            print(f"Total de puntos: {puntos}")
        else:
            print("Te has encontrado un dragón hambriento y te ha comido, no has llegado al final de la mazmorra.")
            print(f"Total de puntos: {puntos}")

        cont += 1

    if not salir:
        print("\nHas ganado! :)\n")
    else:
        print("\nHas perdido :(\n")

    print("¿Desea empezar de nuevo? (s/n)")
    respuesta = input()

    cont = 0
    salir = False

    while not respuesta.lower().__eq__("s") and not respuesta.lower().__eq__("n"):
        print("La respuesta no es correcta")

        print("¿Desea empezar de nuevo? (s/n)")
        respuesta = input()
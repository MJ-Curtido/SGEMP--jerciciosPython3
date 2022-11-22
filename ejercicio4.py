respuesta = "s"

while respuesta.lower().__eq__("s"):
    print("Introduzca una cantidad de dólares:")
    dolares = input()

    print("Introduzca una tasa de interés:")
    tasaInteres = input()

    print("Introduzca un número de años:")
    anyos = input()

    capitalFinal = float(dolares) * (1 + float(tasaInteres) / 100) ** float(anyos);

    print(f"El capital inicial a lo largo de {anyos} años, se ha convertido en {round(capitalFinal * 100) / 100}$")

    print("¿Desea volver a jugar? (s/n)")
    respuesta = input()

    while not respuesta.lower().__eq__("s") and not respuesta.lower().__eq__("n"):
        print("La respuesta no es correcta")

        print("¿Desea volver a jugar? (s/n)")
        respuesta = input()
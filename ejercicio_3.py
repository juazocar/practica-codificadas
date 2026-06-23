n = int(input("Ingrese la cantidad de personas: "))

frecuencias = {}
comunes = None

for i in range(n):

    cantidad_palabras = int(input("Ingrese la cantidad de palabras: "))

    palabras_actuales = set()

    for j in range(cantidad_palabras):

        palabra = input("Ingrese la palabra: ")

        if palabra not in frecuencias:
            frecuencias[palabra] = 1
        else:
            frecuencias[palabra] += 1

        palabras_actuales.add(palabra)

    if comunes is None:
        comunes = palabras_actuales
    else:
        comunes = comunes.intersection(palabras_actuales)

lista_final = []

print(frecuencias)

for palabra in comunes:
    lista_final.append((frecuencias[palabra], palabra))

lista_final.sort(
    key=lambda elemento: (elemento[0], elemento[1]),
    reverse=False
)

for frecuencia, palabra in lista_final:
    print(palabra)
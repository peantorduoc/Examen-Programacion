import csv
import re
import operator
import os

#Leer el archivo CSV
with open("endpoint.csv", "r") as file:
    # Crear un objeto lector CSV con un delimitador de tabulación
    reader = csv.reader(file, delimiter="\t")

    # Saltar la primera línea que contiene los encabezados
    next(reader)

    # Crear un diccionario para contar las palabras
    word_count = {}

    # Recorrer las filas del archivo CSV
    for row in reader:
        text = row[1]  # Obtener el contenido de la columna "texto"
        words = re.findall(r'\b\w+\b', text.lower())  # Obtener las palabras en minúsculas

        # Excluir artículos y conectores de la lista de palabras
        excluded_words = ["a", "an", "the", "and", "or", "but"]
        words = [word for word in words if word not in excluded_words]

        # Contar la frecuencia de las palabras
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    # Obtener las 10 palabras más repetidas
    top_ten = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)[:10]

    # Crear el nuevo archivo de texto "ranking.txt"
    with open("ranking.txt", "w") as new_file:
        new_file.write("Top 10 palabras más repetidas:\n")
        for word, count in top_ten:
            new_file.write(f"{word}: {count}\n")

    # Establecer permisos chmod 400 en el nuevo archivo
    os.chmod("ranking.txt", 0o400)

print("Proceso completado.")
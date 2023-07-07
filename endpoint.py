import requests
import csv

#URL del endpoint
url = "https://dummyjson.com/quotes"

#Realizar una solicitud GET a la URL
response = requests.get(url)

#Obtener los datos JSON de la respuesta
data = response.json()

#Extraer las citas y autores del JSON
quotes = data["quotes"]
autor_texto = [(quote["author"], quote["quote"]) for quote in quotes]

#Abrir un archivo CSV en modo escritura
with open("endpoint.csv", "w", newline="") as file:
    # Crear un objeto escritor CSV con un delimitador de tabulación
    writer = csv.writer(file, delimiter="\t")

#Escribir los datos en el archivo CSV
    writer.writerows(autor_texto)

#Mostrar un mensaje de validación
print("Datos guardados en endpoint.csv")
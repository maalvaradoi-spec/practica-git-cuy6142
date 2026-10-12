#!/usr/bin/env python3
"""Consulta datos de cualquier Pokemon en la API publica PokeAPI."""

import sys
import requests

URL_BASE = "https://pokeapi.co/api/v2/pokemon/"


def consultar(nombre):
    """Pide los datos de un Pokemon a la API y los muestra por pantalla."""
    url = URL_BASE + nombre.strip().lower()
    try:
        respuesta = requests.get(url, timeout=10)
    except requests.RequestException as error:
        print(f"Error de conexion: {error}")
        return

    print(f"Codigo HTTP: {respuesta.status_code}")

    if respuesta.status_code == 404:
        print(f"No se encontro el Pokemon '{nombre}'. Revisa el nombre.")
        return

    if respuesta.status_code != 200:
        print("La API no respondio correctamente.")
        return

    mostrar(respuesta.json())


def mostrar(datos):
    tipos = ", ".join(t["type"]["name"] for t in datos["types"])

    print("-" * 42)
    print(f"Nombre : {datos['name'].title()}")
    print(f"Numero : {datos['id']}")
    print(f"Altura : {datos['height'] / 10} m")
    print(f"Peso   : {datos['weight'] / 10} kg")
    print(f"Tipos  : {tipos}")
    print("Habilidades:")
    for habilidad in datos["abilities"]:
        print(f" - {habilidad['ability']['name']}")
    print("-" * 42)


def main():
    if len(sys.argv) > 1:
        consultar(sys.argv[1])
        return

    print("Consulta de Pokemon - PokeAPI")
    print("Escribe 'salir' para terminar.\n")

    while True:
        nombre = input("Pokemon a consultar: ")
        if nombre.strip().lower() in ("salir", "exit", ""):
            print("Hasta luego.")
            break
        consultar(nombre)


if __name__ == "__main__":
    main()
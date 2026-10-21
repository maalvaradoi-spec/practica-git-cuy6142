import requests

print("Consulta de Pokémon (escribe 'salir' para terminar)")

while True:
    nombre = input("\nNombre o número del Pokémon: ").strip().lower()

    if nombre == "salir":
        print("¡Hasta luego!")
        break
    if nombre == "":
        print("Debes escribir un nombre o número.")
        continue

    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"
    respuesta = requests.get(url, timeout=10)
    print(f"Código HTTP: {respuesta.status_code}")

    if respuesta.status_code == 404:
        print(f"No se encontró el Pokémon '{nombre}'.")
        continue
    respuesta.raise_for_status()
    datos = respuesta.json()

    print(f"Nombre: {datos['name'].title()}")
    print(f"Número: {datos['id']}")
    print(f"Peso: {datos['weight']} hectogramos")
    print("Tipos:")
    for tipo in datos["types"]:
        print(f" - {tipo['type']['name']}")
    print("Habilidades:")
    for habilidad in datos["abilities"]:
        print(f" - {habilidad['ability']['name']}")

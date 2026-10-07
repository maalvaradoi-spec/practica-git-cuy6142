import requests

nombre = "pikachu"
url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"

respuesta = requests.get(url, timeout=10)
print(f"Código HTTP: {respuesta.status_code}")
respuesta.raise_for_status()
datos = respuesta.json()

print(f"Nombre: {datos['name'].title()}")
print(f"Peso: {datos['weight']} hectogramos")
print("Habilidades:")
for habilidad in datos["abilities"]:
    print(f" - {habilidad['ability']['name']}")

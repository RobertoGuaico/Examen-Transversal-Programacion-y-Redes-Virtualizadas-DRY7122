import openrouteservice

client = openrouteservice.Client(
    key='5b3ce3597851110001cf6248afc0c7ab828f4e8fb28eadb494f8a4b5'
)

while True:
    print("Escribe 's' para salir.")
    salida = input("Continuar? (Enter/s): ")
    if salida.lower() == 's':
        break

    origen = input("Ciudad de Origen: ")
    destino = input("Ciudad de Destino: ")
    transporte = input("Medio de transporte (driving-car/foot-walking): ")

    geo_origen = client.pelias_search(text=origen)
    geo_destino = client.pelias_search(text=destino)

    coords = [
        geo_origen['features'][0]['geometry']['coordinates'],
        geo_destino['features'][0]['geometry']['coordinates']
    ]

    ruta = client.directions(coords, profile=transporte)
    distancia_km = ruta['routes'][0]['summary']['distance'] / 1000
    duracion_hr = ruta['routes'][0]['summary']['duration'] / 3600

    print(f"Distancia: {distancia_km:.2f} km")
    print(f"Duración: {duracion_hr:.2f} horas")
    print("Narrativa del viaje:")
    for paso in ruta['routes'][0]['segments'][0]['steps']:
        print("-", paso['instruction'])


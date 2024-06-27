import json

# Diccionario de juegos disponibles en la tienda
juegos_disponibles = {
    "nintendo": [
        {"nombre": "Princess Peach: Showtime!", "tipo": "Aventura", "precio": 27990},
        {"nombre": "Mario vs. Donkey Kong", "tipo": "Aventura", "precio": 31990},
        {"nombre": "Hogwarts Legacy", "tipo": "Aventura", "precio": 28990}
    ],
    "PS5": [
        {"nombre": "METAL SLUG ATTACK RELOADED", "tipo": "Accion", "precio": 9990},
        {"nombre": "Crown Wars", "tipo": "Accion", "precio": 36990},
        {"nombre": "EA SPORTS FC 24 FIFA 24", "tipo": "Deporte", "precio": 26990},
        {"nombre": "TopSpin 2K25", "tipo": "Deporte", "precio": 22990},
        {"nombre": "Rugby 22", "tipo": "Deporte", "precio": 32990}
    ],
    "PS4": [
        {"nombre": "Call of Duty Black Black Ops 6", "tipo": "Disparos", "precio": 42990},
        {"nombre": "Red Dead Redemption + Undead Nightmare", "tipo": "Disparos", "precio": 32990}
    ]
}

# Estructura para almacenar las ventas
ventas = []

# Función para registrar una venta
def registrar_venta():
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    tipo_cliente = input("Ingrese el tipo de cliente (Estudiante, Trabajador, Socio): ")
    tipo_consola = input("Ingrese el tipo de consola (nintendo, PS5, PS4): ")
    
    if tipo_consola in juegos_disponibles:
        print(f"Juegos disponibles para {tipo_consola}:")
        for i, juego in enumerate(juegos_disponibles[tipo_consola], start=1):
            print(f"{i}. {juego['nombre']} - {juego['tipo']} - ${juego['precio']}")
        
        indice_juego = int(input("Seleccione el número del juego: ")) - 1
        if 0 <= indice_juego < len(juegos_disponibles[tipo_consola]):
            juego_seleccionado = juegos_disponibles[tipo_consola][indice_juego]
            tipo_juego = juego_seleccionado["tipo"]
            precio = juego_seleccionado["precio"]
            
            descuento = obtener_descuento(tipo_cliente)
            precio_final = precio - (precio * descuento)
            
            venta = {
                "nombre_cliente": nombre_cliente,
                "tipo_cliente": tipo_cliente,
                "tipo_consola": tipo_consola,
                "tipo_juego": tipo_juego,
                "nombre_juego": juego_seleccionado["nombre"],
                "precio": precio,
                "precio_final": precio_final
            }
            
            ventas.append(venta)
            print("Venta registrada con éxito.")
        else:
            print("Selección de juego no válida.")
    else:
        print("Tipo de consola no válido. Intente de nuevo.")

# Función para mostrar todas las ventas
def mostrar_ventas():
    for venta in ventas:
        print(venta)

# Función para buscar ventas por cliente
def buscar_ventas_por_cliente():
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    ventas_cliente = [venta for venta in ventas if venta["nombre_cliente"] == nombre_cliente]
    for venta in ventas_cliente:
        print(venta)

# Función para guardar las ventas en un archivo
def guardar_ventas():
    with open('ventas.json', 'w') as file:
        json.dump(ventas, file)
    print("Ventas guardadas en el archivo ventas.json")

# Función para cargar las ventas desde un archivo
def cargar_ventas():
    global ventas
    try:
        with open('ventas.json', 'r') as file:
            ventas = json.load(file)
        print("Ventas cargadas desde 'ventas.json'.")
    except FileNotFoundError:
        print("No se encontró el archivo 'ventas.json'.")

# Función para generar factura
def generar_factura():
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    ventas_cliente = [venta for venta in ventas if venta["nombre_cliente"] == nombre_cliente]
    if ventas_cliente:
        print(f"Factura para {nombre_cliente}:")
        total = 0
        for venta in ventas_cliente:
            print(venta)
            total += venta["precio_final"]
        print(f"Total a pagar: {total}")
    else:
        print("No se encontraron ventas para este cliente.")

# Función para obtener el descuento según el tipo de cliente
def obtener_descuento(tipo_cliente):
    if tipo_cliente == "Estudiante":
        return 0.15
    elif tipo_cliente == "Trabajador":
        return 0.10
    elif tipo_cliente == "Socio":
        return 0.20
    else:
        return 0.0

# Menú interactivo
def menu():
    while True:
        print("\nBienvenido al sistema de ventas de juegos de consolas en DUOC UC")
        print("1. Registrar una venta")
        print("2. Mostrar todas las ventas")
        print("3. Buscar ventas por cliente")
        print("4. Guardar las ventas en un archivo")
        print("5. Cargar las ventas desde un archivo")
        print("6. Generar factura")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            mostrar_ventas()
        elif opcion == "3":
            buscar_ventas_por_cliente()
        elif opcion == "4":
            guardar_ventas()
        elif opcion == "5":
            cargar_ventas()
        elif opcion == "6":
            generar_factura()
        elif opcion == "7":
            print("Gracias por usar el sistema de ventas.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

# Ejecutar el menú
menu()

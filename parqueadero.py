import datetime

# Inicialización del parqueadero
vehiculos = ['v' + str(i) for i in range(1, 51)]  # Espacios para carros v1 a v50
motos = ['m' + str(i) for i in range(1, 26)]  # Espacios para motos m1 a m25
parqueadero = vehiculos + motos
estados = {espacio: espacio for espacio in parqueadero}  # Inicialmente todos los espacios están disponibles

# Diccionario para registrar horas de entrada y salida
registros = {}

# Mensaje de bienvenida
def mostrar_bienvenida():
    print("********************************")
    print("¡Bienvenido al parqueadero!")
    print("********************************")

# Función para mostrar el estado del parqueadero
def mostrar_matriz():
    print("***************************************")
    for i in range(0, 50, 10):  # Mostrar 10 carros por línea
        print("-".join(estados[vehiculos[i + j]] for j in range(10)))
    print("***************************************")
    for i in range(0, 25, 10):  # Mostrar 10 motos por línea
        print("-".join(estados[motos[i + j]] for j in range(10 if i + 10 <= 25 else 5)))
    print("***************************************")

# Función para registrar un alquiler
def alquilar_espacio():
    tipo = input("¿Qué tipo de vehículo desea alquilar (carro/moto)? ").lower()
    placa = input("Ingrese la placa del carro/moto: ").upper()
    
    if tipo == "carro":
        disponibles = [v for v in vehiculos if estados[v] == v]
    elif tipo == "moto":
        disponibles = [m for m in motos if estados[m] == m]
    else:
        print("Tipo inválido.")
        return

    if disponibles:
        espacio = disponibles[0]
        estados[espacio] = 'A'
        registros[placa] = {"tipo": tipo, "espacio": espacio, "hora_entrada": None, "hora_salida": None, "alquiler": True}
        print(f"El espacio {espacio} ha sido alquilado al carro/moto con placa {placa}.")
    else:
        print(f"No hay espacios disponibles para {tipo}.")

# Función para registrar la entrada de un carro/moto
def registrar_entrada():
    tipo = input("¿Qué tipo de vehículo desea registrar (carro/moto)? ").lower()
    placa = input("Ingrese la placa del carro/moto: ").upper()
    
    if tipo == "carro":
        disponibles = [v for v in vehiculos if estados[v] == v]
    elif tipo == "moto":
        disponibles = [m for m in motos if estados[m] == m]
    else:
        print("Tipo inválido.")
        return
    
    if disponibles:
        espacio = disponibles[0]
        estados[espacio] = 'O'
        hora_entrada = datetime.datetime.now()
        registros[placa] = {"tipo": tipo, "espacio": espacio, "hora_entrada": hora_entrada, "hora_salida": None, "alquiler": False}
        print(f"Carro/moto {placa} registrado en espacio {espacio} a las {hora_entrada}.")
    else:
        print(f"No hay espacios disponibles para {tipo}.")

# Función para registrar la salida del carro/moto
def registrar_salida():
    placa = input("Ingrese la placa del carro/moto que va a salir: ").upper()
    if placa in registros and registros[placa]["hora_entrada"]:
        espacio = registros[placa]["espacio"]
        registros[placa]["hora_salida"] = datetime.datetime.now()
        estados[espacio] = espacio  # Liberar el espacio
        print(f"Carro/moto con placa {placa} ha salido del espacio {espacio}.")
    else:
        print("Placa no registrada o no tiene entrada registrada.")

# Función para calcular la tarifa
def calcular_tarifa():
    placa = input("Ingrese la placa del carro/moto: ").upper()
    if placa in registros and registros[placa]["hora_entrada"] and registros[placa]["hora_salida"]:
        tiempo_total = registros[placa]["hora_salida"] - registros[placa]["hora_entrada"]
        horas = tiempo_total.total_seconds() // 3600 + 1  # Redondear a la siguiente hora
        tarifa_por_hora = 5  # Tarifa base por hora
        
        # Aplicar descuento si el cliente ocupó más del 70% de la jornada
        horas_totales_jornada = 16  # Jornada de 6am a 10pm (16 horas)
        descuento = 0.15 if horas >= 0.7 * horas_totales_jornada and not registros[placa]["alquiler"] else 0
        
        tarifa_total = horas * tarifa_por_hora * (1 - descuento)
        print(f"El tiempo total fue de {horas:.0f} horas. Tarifa total a pagar: ${tarifa_total:.2f}")
    else:
        print("Placa no registrada correctamente o no tiene registro de salida.")

# Función para actualizar el estado del parqueadero
def actualizar():
    print("Actualizando matriz del parqueadero...")
    mostrar_matriz()

# Menú principal
def menu():
    while True:
        print("\nMenú:")
        print("1. Mostrar matriz del parqueadero")
        print("2. Alquiler")
        print("3. Registrar entrada")
        print("4. Registrar salida")
        print("5. Facturar")
        print("6. Actualizar")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_matriz()
        elif opcion == "2":
            alquilar_espacio()
        elif opcion == "3":
            registrar_entrada()
        elif opcion == "4":
            registrar_salida()
        elif opcion == "5":
            calcular_tarifa()
        elif opcion == "6":
            actualizar()
        elif opcion == "7":
            print("Gracias por usar el sistema de parqueadero. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecución del programa
mostrar_bienvenida()
menu()

#Vamos a crear un sistema de reservas para un hotel.
# En este sistema, tendremos clases para el Hotel, las Habitaciones y las Reservas.

# hotel.py

class Hotel:
    def __init__(self, nombre): #Inicializa el hotel con un nombre, lista de habitaciones y lista de reservas.
        self.nombre = nombre
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, habitacion): # Añade una nueva habitación al hotel.
        self.habitaciones.append(habitacion)

    def hacer_reserva(self, cliente, habitacion_numero, dias): #Crea una nueva reserva si la habitación está disponible.
        for habitacion in self.habitaciones:
            if habitacion.numero == habitacion_numero and habitacion.disponible:
                nueva_reserva = Reserva(cliente, habitacion, dias)
                self.reservas.append(nueva_reserva)
                habitacion.disponible = False
                return f"Reserva realizada para {cliente} en la habitación {habitacion.numero} por {dias} días."
        return "Habitación no disponible."

    def cancelar_reserva(self, cliente, habitacion_numero): #Cancela una reserva específica si existe.
        for reserva in self.reservas:
            if reserva.cliente == cliente and reserva.habitacion.numero == habitacion_numero:
                reserva.habitacion.disponible = True
                self.reservas.remove(reserva)
                return f"Reserva cancelada para {cliente} en la habitación {habitacion_numero}."
        return "Reserva no encontrada."

    def mostrar_reservas(self): # Muestra todas las reservas actuales en el hotel.
        if not self.reservas:
            return "No hay reservas."
        resultado = "Reservas actuales:\n"
        for reserva in self.reservas:
            resultado += f"Cliente: {reserva.cliente}, Habitación: {reserva.habitacion.numero}, Días: {reserva.dias}\n"
        return resultado

class Habitacion:
    def __init__(self, numero, tipo): #Inicializa una habitación con un número, tipo y estado de disponibilidad.
        self.numero = numero
        self.tipo = tipo
        self.disponible = True

class Reserva:
    def __init__(self, cliente, habitacion, dias): #Inicializa una reserva con el cliente, la habitación y la duración de la estancia.
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias

# Ejemplo de uso

if __name__ == "__main__":
    hotel = Hotel("Hotel San Carlos")

    # Agregar habitaciones
    hotel.agregar_habitacion(Habitacion(101, "Sencilla"))
    hotel.agregar_habitacion(Habitacion(102, "Doble"))

    # Realizar reservas
    print(hotel.hacer_reserva("Brayan Camacho", 101, 3))
    print(hotel.hacer_reserva("Ana Pérez", 102, 2))

    # Mostrar reservas actuales
    print(hotel.mostrar_reservas())

    # Cancelar una reserva
    print(hotel.cancelar_reserva("Brayan Camacho", 101))

    # Mostrar reservas después de la cancelación
    print(hotel.mostrar_reservas())

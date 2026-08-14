class Persona:
    # Constructor to initialize the attributes
   def __init__(self, nombre, edad):
        self.nombre = nombre  # attributo nombre
        self.edad = edad      # attributo edad

    # Method to perform an action
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

    # Magic method to print a readable string representation of the object
    def __str__(self):
        return f"Persona(Nombre: {self.nombre}, Edad: {self.edad})"

# --- Test de Class ---

# 1. Crea instancias de (objetos) de la Class Persona
persona1 = Persona("Ana", 28)
persona2 = Persona("Carlos", 35)

# 2. Acceso a attributos
print(persona1.nombre)  # Salida: Ana
print(persona2.edad)    # Salida: 35

# 3. Llamada a metodos
print(persona1.saludar())  # Salida: Hola, mi nombre es Ana y tengo 28 años.

# 4. Imprime el objeto directamente (triggers __str__)
print(persona2)  # Salida: Persona(Nombre: Carlos, Edad: 35)

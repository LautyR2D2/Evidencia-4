class MaquinaDePerfumes:
    def __init__(self, alcohol=0, aceites_esenciales=0, agua=0):
        # Inicializa los ingredientes y olores con los valores proporcionados o 0 si no se proporciona ningún valor
        self.alcohol = alcohol
        self.aceites_esenciales = aceites_esenciales
        self.agua = agua
        self.olores = {}  # Diccionario para almacenar olores y sus cantidades
        self.recetas = {}  # Diccionario para almacenar recetas

    def agregar_ingrediente(self, ingrediente, cantidad):
        # Agrega una cantidad específica de un ingrediente
        if ingrediente == 'alcohol':
            self.alcohol += cantidad
        elif ingrediente == 'aceites_esenciales':
            self.aceites_esenciales += cantidad
        elif ingrediente == 'agua':
            self.agua += cantidad
        else:
            raise ValueError("Ingrediente no reconocido. Use 'alcohol', 'aceites_esenciales' o 'agua'.")

    def agregar_olor(self, olor, cantidad):
        # Agrega un olor específico con su cantidad
        if olor in self.olores:
            self.olores[olor] += cantidad
        else:
            self.olores[olor] = cantidad

    def agregar_receta(self, nombre_receta, receta):
        # Agrega una receta a la lista de recetas
        if not isinstance(receta, dict):
            raise ValueError("La receta debe ser un diccionario con ingredientes y olores.")
        self.recetas[nombre_receta] = receta

    def seguir_receta(self, nombre_receta):
        # Sigue una receta específica
        if nombre_receta in self.recetas:
            receta = self.recetas[nombre_receta]
            self.alcohol = receta.get('alcohol', 0)
            self.aceites_esenciales = receta.get('aceites_esenciales', 0)
            self.agua = receta.get('agua', 0)
            self.olores = receta.get('olores', {})
            return f"Receta '{nombre_receta}' aplicada: Alcohol: {self.alcohol} ml, Aceites Esenciales: {self.aceites_esenciales} ml, Agua: {self.agua} ml, Olores: {self.olores}"
        else:
            raise ValueError("Receta no encontrada.")

    def mezclar_ingredientes(self):
        # Mezcla los ingredientes y retorna el estado actual de la mezcla
        volumen_total = self.alcohol + self.aceites_esenciales + self.agua
        if volumen_total == 0:
            raise ValueError("No hay ingredientes para mezclar.")
        return (f"Mezcla completa: Alcohol: {self.alcohol} ml, "
                f"Aceites Esenciales: {self.aceites_esenciales} ml, "
                f"Agua: {self.agua} ml, Olores: {self.olores}")

    def __str__(self):
        # Representación en cadena de la máquina
        olores_str = ', '.join([f"{olor}: {cantidad} ml" for olor, cantidad in self.olores.items()])
        return (f"Estado actual de la Máquina de Perfumes:\n"
                f"Alcohol: {self.alcohol} ml\n"
                f"Aceites Esenciales: {self.aceites_esenciales} ml\n"
                f"Agua: {self.agua} ml\n"
                f"Olores: {olores_str}")

# Crear una instancia de la máquina
maquina = MaquinaDePerfumes()

# Agregar recetas
maquina.agregar_receta('Perfume Floral', {
    'alcohol': 80,
    'aceites_esenciales': 15,
    'agua': 5,
    'olores': {'Rosa': 10, 'Jazmín': 5}
})

maquina.agregar_receta('Perfume Amaderado', {
    'alcohol': 70,
    'aceites_esenciales': 20,
    'agua': 10,
    'olores': {'Sándalo': 15, 'Cedro': 10}
})

# Aplicar una receta
print(maquina.seguir_receta('Perfume Floral'))

# Ver el estado actual
print(maquina)

# Mezclar ingredientes
print(maquina.mezclar_ingredientes())
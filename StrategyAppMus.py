# Patrón Strategy aplicado a recomendaciones musicales por Christian Lara

# Clase base de estrategia
class EstrategiaRecomendacion:
    def recomendar(self, usuario):
        # Este método será implementado por las clases hijas
        pass

# Estrategia 1: Recomendaciones basadas en el género favorito del usuario
class PorGeneroFavorito(EstrategiaRecomendacion):
    def recomendar(self, usuario):
        return f"🎶 Recomendando canciones del género: {usuario['genero_favorito']}"

# Estrategia 2: Recomendaciones basadas en el historial de escucha
class PorHistorial(EstrategiaRecomendacion):
    def recomendar(self, usuario):
        canciones = ', '.join(usuario['ultimas_canciones'])
        return f"🔁 Basado en tu historial: {canciones}"

# Estrategia 3: Recomendaciones basadas en popularidad global
class PorPopularidad(EstrategiaRecomendacion):
    def recomendar(self, usuario):
        return "🔥 Estas son las canciones más populares globalmente ahora mismo."

# Clase Recomendador que usará diferentes estrategias
class Recomendador:
    def __init__(self, estrategia):
        # Inicializa el recomendador con una estrategia específica
        self.estrategia = estrategia

    def mostrar_recomendaciones(self, usuario):
        # Ejecuta la estrategia actual sobre el usuario
        return self.estrategia.recomendar(usuario)

# ---------------- USO DEL STRATEGY ------------------

# Simulamos un usuario
usuario = {
    "nombre": "Chris",
    "genero_favorito": "Rock Alternativo",
    "ultimas_canciones": ["In the End", "Numb", "Chop Suey"]
}

# Creamos el recomendador con una estrategia inicial
recomendador = Recomendador(PorGeneroFavorito())
print(recomendador.mostrar_recomendaciones(usuario))  # Usa género favorito

# Cambiamos la estrategia a historial
recomendador.estrategia = PorHistorial()
print(recomendador.mostrar_recomendaciones(usuario))  # Usa historial

# Cambiamos la estrategia a popularidad global
recomendador.estrategia = PorPopularidad()
print(recomendador.mostrar_recomendaciones(usuario))  # Usa popularidad

class EstrategiaRecomendacion:
    def recomendar(self, usuario):
        pass
class PorGeneroFavorito(EstrategiaRecomendacion):
    def recomendar(self, usuario):
        return f"🎶 Recomendando canciones del género: {usuario['genero_favorito']}"
class PorHistorial(EstrategiaRecomendacion):
    def recomendar(self, usuario):
        canciones = ', '.join(usuario['ultimas_canciones'])
        return f"🔁 Basado en tu historial: {canciones}"
class PorPopularidad(EstrategiaRecomendacion):
    def recomendar(self, usuario):
        return "🔥 Estas son las canciones más populares globalmente ahora mismo."
class Recomendador:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def mostrar_recomendaciones(self, usuario):
        return self.estrategia.recomendar(usuario)

usuario = {
    "nombre": "Chris",
    "genero_favorito": "Rap",
    "ultimas_canciones": ["El juego que juegas", "4rabe", "Luz"]
}

recomendador = Recomendador(PorGeneroFavorito())
print(recomendador.mostrar_recomendaciones(usuario))
recomendador.estrategia = PorHistorial()
print(recomendador.mostrar_recomendaciones(usuario))
recomendador.estrategia = PorPopularidad()
print(recomendador.mostrar_recomendaciones(usuario))
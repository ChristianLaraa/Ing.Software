class ConfiguracionMusical:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("🎵 Inicializando Configuración Global Musical...")
            cls._instancia = super().__new__(cls)

            cls._instancia.calidad = "Alta"
            cls._instancia.idioma = "Español"
            cls._instancia.usuario_activo = "usuario123"
        return cls._instancia

config1 = ConfiguracionMusical()
config2 = ConfiguracionMusical()

print("Usuario activo (config1):", config1.usuario_activo)
print("Usuario activo (config2):", config2.usuario_activo)

print("¿Ambas configuraciones son la misma instancia?", config1 is config2)

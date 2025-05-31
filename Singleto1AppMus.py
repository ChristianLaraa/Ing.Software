# Patrón Singleton aplicado a la configuración global de una app musical por Christian Lara

class ConfiguracionMusical:
    # Variable de clase que almacenará la única instancia de ConfiguracionMusical
    _instancia = None

    def __new__(cls):
        # Si no existe una instancia, la creamos
        if cls._instancia is None:
            print("🎵 Inicializando Configuración Global Musical...")
            cls._instancia = super().__new__(cls)

            # Asignamos valores por defecto a la configuración
            cls._instancia.calidad = "Alta"
            cls._instancia.idioma = "Español"
            cls._instancia.usuario_activo = "usuario123"
        # Si ya existe una instancia, simplemente la retornamos
        return cls._instancia


# ---------------- USO DEL SINGLETON ------------------

# Intentamos crear dos configuraciones distintas
config1 = ConfiguracionMusical()
config2 = ConfiguracionMusical()

# Mostramos el usuario activo desde ambas "instancias"
print("Usuario activo (config1):", config1.usuario_activo)
print("Usuario activo (config2):", config2.usuario_activo)

# Comprobamos si ambas variables apuntan a la misma instancia
print("¿Ambas configuraciones son la misma instancia?", config1 is config2)

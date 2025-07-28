import os

# Lista de nombres
nombres = [
  #TODO NOMBRES DE LAS CARPETAS
]

# Ruta base (puedes cambiarla a donde quieras crear las carpetas)
ruta_base = "./ParticipantesFranci"

# Crear carpeta base si no existe
os.makedirs(ruta_base, exist_ok=True)

# Crear carpetas por nombre y sesiones
for nombre in nombres:
    carpeta_participante = os.path.join(ruta_base, nombre)
    os.makedirs(carpeta_participante, exist_ok=True)
    for i in range(1, 6):
        carpeta_sesion = os.path.join(carpeta_participante, f"sesión {i}")
        os.makedirs(carpeta_sesion, exist_ok=True)

print("¡Carpetas creadas exitosamente!", ruta_base)

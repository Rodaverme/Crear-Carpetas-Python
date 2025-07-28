import os

# Lista de nombres
nombres = [
   "VALERIA DIAZ VELASQUEZ", 
   "LINA MARCELA ARBELAEZ OMEZ", 
   "CARLOS EDUARDO GUAÑARITA REYES", 
   "FERNANDA VILLANI MINOTA", "JEAN CARLO GUERERO LOPEZ", "DYLAN ANDRES MORENO LONDOÑO", "ANDRES FERNANDO MONTOYA FERNANDEZ",
    "MAGNOLIA DIAZ RAMOS", "DAVID ALEXANDER CABALLERO OBANDO", "HECTOR FAURO VARGAS GUTIERREZ", "LINA MARIA CAICEDO RIOS", "KATHERINE ROJAS SALAS",
    "GUSTAVO ADOLFO CABRERA ABELLA", "CESAR ALBERTO ROA GOMEZ", "JUAN ESTEBAN PINCHAO BUENO", "PEDRO REYNEL HERNANDEZ DE LOS REYES", 
       "MARIANA STEFANIA SALAZAR GONZALEZ", "SARA SILVA PLAZA", "JULIAN ANDRES SANCHEZ QUINTERO", "SERGIO ANDRES SILVA ARROYO", "ALEJANDRO OROZCO",
         "MARCELA PABON HERRERA", "CLAUDIA BRIÑEZ SANCHEZ", "GUSTAVO ADOLFO CORTES AYALA", "IVAN FERNANDO ZARAMA PEPINOSA", "PAOLA ANDREA LONDOÑO LOPEZ", 
         "CRISTOBAL MUÑOZ ORDOÑEZ", "LUISA MARIA PATIÑO CERTUCHE", "YULIANA CAROLINA HERRERA", "KEVIN STEVEN VILLAMIL CARDONA"
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

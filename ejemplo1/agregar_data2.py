from sqlalchemy.orm import sessionmaker
from crear_base import Saludo
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()


with open("/home/raul/PlataformasWeb/clase06-1bim-raul8005/ejemplo1/data/saludos_mundo.csv", "r", encoding="utf-8") as archivo:
    next(archivo)  # Saltar la línea del encabezado

    for linea in archivo:
        partes = linea.strip().split("|")  # Separar por "|"

        if len(partes) >= 2:
            mensaje = partes[0]
            tipo = partes[1]

            saludo = Saludo(mensaje=mensaje, tipo=tipo)
            session.add(saludo)

# Guardar cambios
session.commit()

from sqlalchemy.orm import sessionmaker

from crear_base import Saludo
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

with open("../Data/saludos_mundos.csv", "r", encoding="utf-8") as archivo:
	next(archivo)  # Saltar linea por linea del archivo
    for linea in archivo:
        partes = linea.strip().split("|") 
        if len(partes) == 3:
            mensaje, tipo, origen = partes
            saludo = Saludo(mensaje=mensaje, tipo=tipo, origen=origen)
            session.add(saludo)


#Guardar cambios
session.commit()

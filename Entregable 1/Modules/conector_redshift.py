import sqlalchemy as sa
from sqlalchemy.engine.url import URL
import os

class DatabaseConnector:
    def conector(self):
        with open('Entregable 1\Modules\datos_conexion.txt') as f:
            lines = f.readlines()
            host  = lines[0].strip()
            port = lines[1].strip()
            database = lines[2].strip()
            usuario = lines[3].strip()
            clave = lines[4].strip()

        url = URL.create(
        drivername='redshift+redshift_connector', 
        host=host,
        port=port,
        database=database,
        username=usuario,
        password=clave,
        )
        engine = sa.create_engine(url)

        return engine


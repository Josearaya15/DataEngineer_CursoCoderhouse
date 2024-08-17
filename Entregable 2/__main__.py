import sqlalchemy as sa
from sqlalchemy.engine.url import URL
import os
from Modules.conector_redshift import DatabaseConnector
from Modules.import_api import API
import pandas as pd

conn = DatabaseConnector()
engine = conn.conector()

API = API()
df = API.getdata()


#Creación de tabla
Path_CreacionTabla = 'Comandos_SQL/creacion_tabla.sql'

with engine.connect() as connection:
    with open(Path_CreacionTabla, 'r') as sql_file:
        sql_creaciontabla = sql_file.read()

    connection.execute(sql_creaciontabla)

#Carga tabla a redshift
    df.to_sql(name = 'turnosfarmaciaschile',
              con = connection,
              if_exists = 'append',
              schema = 'joseignacioaraya15_coderhouse', 
              index = False, 
              method = 'multi')
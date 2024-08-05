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

with engine.connect() as connection:
    df.to_sql(name = 'turnosfarmaciaschile',con = connection,if_exists = 'append', schema = 'joseignacioaraya15_coderhouse', index = False)
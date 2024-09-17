import sqlalchemy as sa
from sqlalchemy.engine.url import URL
import os
from dotenv import load_dotenv
from sqlalchemy.exc import SQLAlchemyError

load_dotenv()

class DatabaseConnector:
    def conector(self):
        
        url = URL.create(
        drivername='redshift+psycopg2', 
        host=os.getenv('host'),
        port=os.getenv('port'),
        database=os.getenv('database'),
        username=os.getenv('usuario'),
        password=os.getenv('password')
        )



        try:
            engine = sa.create_engine(url)
            print("Conexión exitosa a la base de datos.")
            return engine
        
        except SQLAlchemyError as e:
            print(f"Error al conectar a la base de datos: {str(e)}")
            return None



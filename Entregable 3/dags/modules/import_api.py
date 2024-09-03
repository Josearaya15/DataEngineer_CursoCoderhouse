import requests
import pandas as pd
from datetime import datetime

class API:
    def getdata(self):
        r = requests.get('https://midas.minsal.cl/farmacia_v2/WS/getLocalesTurnos.php')
        j = r.json()
        df = pd.DataFrame.from_dict(j)
        
        #ID Unico
        df['ID'] = df['fecha'] + '-' + df['local_id'] + '-' + df['fk_region']+ '-'+ df['fk_comuna']+'-'+ df['fk_localidad']
        #Fecha ingesta
        df['Fecha_Ingesta'] = datetime.now()
        
        #Guardar CSV temporal
        df.to_csv('/opt/airflow/dags/temp/df_pandas.csv')
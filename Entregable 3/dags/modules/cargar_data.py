import pandas as pd
from airflow.providers.amazon.aws.hooks.redshift_sql import RedshiftSQLHook

class CargaDatos:

      def carga_datos(self):
            
      #Carga tabla a redshift

            hook = RedshiftSQLHook(redshift_conn_id='redshift_default')
            engine = hook.get_sqlalchemy_engine()

            df = pd.read_csv('/opt/airflow/dags/temp/df_pandas.csv')

            df.drop(df.columns[0],axis=1,inplace=True)
            
            df.to_sql(name = 'turnosfarmaciaschile',
                  con = engine,
                  if_exists = 'append',
                  schema = 'joseignacioaraya15_coderhouse', 
                  index = False, 
                  method = 'multi')
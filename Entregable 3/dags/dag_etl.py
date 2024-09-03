from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from modules.import_api import API
from modules.cargar_data import CargaDatos

def extraer_datos_API():
    api_instance = API()
    api_instance.getdata()

def carga_datos_task():
    carga_datos_instanciado = CargaDatos()  
    carga_datos_instanciado.carga_datos()  

default_args={
    'owner': 'jose_araya',
    'retries':5,
    'retry_delay': timedelta(minutes=3)
}

DAG_ID = "redshift_etl_dag"

with DAG(
    default_args=default_args,
    dag_id=DAG_ID,
    description= 'Dag conexion y carga datos a redshift',
    start_date=datetime(2024,9,2),
    schedule_interval='@daily',
    catchup=False
    ) as dag:


        #Tasks
        # 1 extraer info. de api a un df
        task_extraer_API = PythonOperator(
                task_id='extrear_datos_API',
                python_callable=extraer_datos_API
        )

        # 2 cargar datos a redshift
        task_cargar_datos = PythonOperator(
                task_id='cargar_datos',
                python_callable=carga_datos_task
        )

        ##Dependencias Task

        task_extraer_API >> task_cargar_datos
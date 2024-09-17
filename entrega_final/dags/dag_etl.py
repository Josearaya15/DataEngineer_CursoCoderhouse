from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from modules.import_api import API
from modules.cargar_data import CargaDatos
from modules.mail_sender import send_email

def extraer_datos_API():
    api_instance = API()
    api_instance.getdata()

def carga_datos_task():
    carga_datos_instanciado = CargaDatos()  
    carga_datos_instanciado.carga_datos()  

default_args={
    'owner': 'jose_araya',
    'start_date': datetime.now(),
    'email': ['joseignacioaraya15@gmail.com'],
    'retries':3,
    'retry_delay': timedelta(seconds=30),
    'depends_on_past': False,
    'email_on_retry':True,
    'email_on_failure': True,
    'catchup':False
}


with DAG(
    default_args=default_args,
    dag_id="redshift_etl_dag",
    description= 'Dag conexion y carga datos a redshift',
    schedule_interval='@daily',

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

        # 3 enviar mail de confirmación
        task_send_mail = PythonOperator(
                task_id='mail_sender',
                python_callable=send_email
        )

        ##Dependencias Task

        task_extraer_API >> task_cargar_datos >>  task_send_mail  
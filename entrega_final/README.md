### Integración turnos de farmacias Chile desde API publica a Redshift

## Este proyecto es un flujo de integración de datos desde una API publica a una base de datos en Redshift.

Para iniciar este proyecto, deben ingresar en la terminal a la ruta **.../entrega_final** , luego debe ejecutar los siguientes comandos en consola:

``` bash
mkdir -p ./{logs,dags,config,plugins}
```

El archivo .env con las variables de entorno debe posee la siguiente estructura:

```
AIRFLOW_UID= 
# Lista de emails para funcion mail_sender, estas deben entre comillas separados por ; en caso de ser más de 1
EMAIL_CONFIRMACION =
SMTP_HOST=
SMTP_STARTTLS= 
SMTP_SSL= 
SMTP_USER= 
SMTP_PASSWORD= 
SMTP_PORT= 
SMTP_MAIL_FROM= 
```

Posteriormente, deben ejecutar en la terminal:

``` bash
docker compose airflow-init
docker compose up
```

Luego debe ingresar a airflow en un navegador en dirección **localhost:8080**, ingresar con su usuario y contraseña, en este caso de desarrollo es el usuario **"airflow"** y contraseña **"airflow** por defecto.

Ya dentro del aplicativo debe dirigirse a **Admin -> Connections** y crear una conexión a **Amazon Redshift** con 
**Connection id = redshift_default**.

Finalmente active el dag en airflow para su ejecución diaria.
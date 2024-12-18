from asyncio import tasks
from nis import cat
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from dags.cities.sao_paulo import sao_paulo
from dags.cities.df import df
from dags.cities.rio import rio
from dags.cities.buenos_aires import buenos_aires
from dags.cities.curitiba import curitiba

with DAG("cities",
    start_date=datetime(2022, 9, 16),
    schedule_interval=timedelta(seconds=60),
    catchup=False
) as dag:
    sp_task = PythonOperator(
        task_id= "sp",
        python_callable=sao_paulo
    )

    df_task = PythonOperator(
        task_id= "df",
        python_callable=df
    )

    rio_task = PythonOperator(
        task_id= "rio",
        python_callable=rio
    )

    buenos_aires_task = PythonOperator(
        task_id= "buenos_aires",
        python_callable=buenos_aires
    )
    
    curitiba_task = PythonOperator(
        task_id= "curitiba",
        python_callable=curitiba
    )
    
    sp_task >> df_task >> rio_task >> buenos_aires_task >> curitiba_task

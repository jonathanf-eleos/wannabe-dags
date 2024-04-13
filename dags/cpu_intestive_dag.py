from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import time
import random
from datetime import datetime


def cpu_intensive_task():
    # Simulate CPU-intensive computation
    for _ in range(10**7):
        random.random()

dag = DAG(
    'cpu_intensive_dag',
    schedule_interval=None,
    catchup=False,
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2024, 4, 13),
    },
)

task_cpu_intensive = PythonOperator(
    task_id='cpu_intensive_task',
    python_callable=cpu_intensive_task,
    dag=dag,
)

task_cpu_intensive

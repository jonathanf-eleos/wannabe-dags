from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import numpy as np
from datetime import datetime


def memory_intensive_task():
    # Simulate memory-intensive operation
    large_array = np.random.rand(10**7)

dag = DAG(
    'memory_intensive_dag',
    schedule_interval=None,
    catchup=False,
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2024, 4, 13),
    },
)

task_memory_intensive = PythonOperator(
    task_id='memory_intensive_task',
    python_callable=memory_intensive_task,
    dag=dag,
)

task_memory_intensive

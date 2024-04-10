from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="python_operator_dag", start_date=datetime(2022, 1, 1), schedule=None) as dag:
    # Tasks are represented as operators

    @task()
    def airflow():
        print("This is a python operator")

    @task()
    def flowair():
        print("Eenie meenie minei mo")
    # Set dependencies between tasks
    airflow() >> flowair()
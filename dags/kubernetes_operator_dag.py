from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from datetime import datetime

from airflow import DAG

# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="kubernetes_operator_dag", start_date=datetime(2022, 1, 1), schedule=None) as dag:
    # Tasks are represented as operators
    k = KubernetesPodOperator(
        name="hello-dry-run",
        image="debian",
        cmds=["bash", "-cx"],
        arguments=["echo", "10"],
        labels={"foo": "bar"},
        task_id="dry_run_demo",
        do_xcom_push=True,
    )

    k.dry_run()
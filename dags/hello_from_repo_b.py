from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="hello_from_repo_b",
    schedule="@daily",
    start_date=datetime(2026, 5, 1),
    catchup=False,
    tags=["bundle-b"],
) as dag:
    BashOperator(task_id="hello_b", bash_command="echo 'I am from repo B'")

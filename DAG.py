from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define the function that performs the task
def my_task():
    # Your code here
    print("Hello, Airflow!")

# Define the DAG
dag = DAG(
    'my_dag',
    description='My DAG',
    schedule_interval='0 0 * * *',
    start_date=datetime(2021, 1, 1),
    catchup=False
)

# Create a task using the PythonOperator
task = PythonOperator(
    task_id='my_task',
    python_callable=my_task,
    dag=dag
)
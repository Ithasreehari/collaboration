from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    'gcs_to_bigquery_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['gcp', 'bigquery', 'gcs'],
) as dag:

    # Task 1: Load data from GCS to BigQuery
    load_csv_to_bq = GCSToBigQueryOperator(
        task_id='load_csv_to_bq',
        bucket='itha-bucket',
        source_objects=['students.csv'],
        destination_project_dataset_table='ithaproj1.mydataset.student',
        source_format='CSV',
        skip_leading_rows=1,
        autodetect=True,
        write_disposition='WRITE_TRUNCATE',
    )

    # Task 2: Run a SQL query on the BigQuery table
    run_bq_query = BigQueryInsertJobOperator(
        task_id='run_bq_query',
        configuration={
            "query": {
                "query": "SELECT * FROM ithaproj1.mydataset.student LIMIT 10;",
                "useLegacySql": False,
            }
        }
    )

    load_csv_to_bq >> run_bq_query

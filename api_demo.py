from google.cloud import bigquery
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'application_default_credentials.json'
client = bigquery.Client(project='mimetic-slice-343817')
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=True,
)

def load_data_from_datalake():
    query_job = client.query(
    """
    SELECT sentence, sentiment FROM `mimetic-slice-343817.vi_student_feedbacks.data` LIMIT 10""")
    results = query_job.result()
    return results.to_dataframe()

def load_cleaned_data():
    query_job = client.query(
    """
    SELECT sentence, sentiment FROM `mimetic-slice-343817.vi_student_feedbacks.data_clean`""")
    results = query_job.result()
    return results.to_dataframe()

def load_unlabeled_data():
    query_job = client.query(
    """
    SELECT sentence, sentiment FROM `mimetic-slice-343817.vi_student_feedbacks.data_unlabeled`""")
    results = query_job.result()
    return results.to_dataframe()

def push_cleaned_data():
    file_path = 'data/data_clean.csv'
    table_id = 'mimetic-slice-343817.vi_student_feedbacks.data_clean'
    with open(file_path, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_id, job_config=job_config)
    job.result()  # Waits for the job to complete.


def push_unlabeled_data():
    file_path = 'data/data_unlabeled.csv'
    table_id = 'mimetic-slice-343817.vi_student_feedbacks.data_unlabeled'
    with open(file_path, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_id, job_config=job_config)
    job.result()  # Waits for the job to complete.

print(load_data_from_datalake())
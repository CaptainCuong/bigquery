from google.cloud import bigquery
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'application_default_credentials.json'
client = bigquery.Client(project='mimetic-slice-343817')

query_job = client.query(
    """
    SELECT age FROM `mimetic-slice-343817.banking.train` LIMIT 10"""
)

results = query_job.result()  # Waits for job to complete.
print(results.to_dataframe())
# for row in results:
# 	print(row['age'])
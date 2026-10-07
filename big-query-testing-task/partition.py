from google.cloud import bigquery

client = bigquery.Client()

def scanned(table):
    job = client.query(
    f"SELECT * FROM `{table}`"
    f"WHERE DATE(created_at) = '2023-06-01'",
    job_config=bigquery.QueryJobConfig(dry_run=True),
    )
    return job.total_bytes_processed

client.query("""
CREATE OR REPLACE TABLE `sample-table`
PARTITION BY DATE(created_at) AS
SELECT * FROM `source-table`
""").result()

a = scanned("sample-table")
b = scanned("source-table")
print(f"Bytes processed for partitioned table: {a}")
print(f"Bytes processed for non-partitioned table: {b}")
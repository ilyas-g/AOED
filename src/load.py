from google.cloud import bigquery

def load_jobs(jobs):

    client = bigquery.Client()
    client.load_table_from_json(jobs, "aoed-498221.jobs_data.jobs_raw")
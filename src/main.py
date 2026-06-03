from extract import extract_jobs
from load import load_jobs

jobs = extract_jobs()
load_jobs(jobs)
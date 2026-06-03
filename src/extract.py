import requests
from dotenv import API_KEY, API_ID

def extract_jobs():

    url = f"http://api.adzuna.com/v1/api/jobs/gb/version?app_id={API_ID}&app_key={API_KEY}&&content-type=application/json"

    response = requests.get(url)

    jobs = response.json()

    return jobs
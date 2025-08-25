from airflow.decorators import dag, task
from airflow.models import Variable
from pendulum import datetime
import requests
import logging

API = "https://www.boreapi.com/api/activity"

@dag(
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    tags=["activity"],
    catchup=False,
)
def find_activity():
    @task
    def get_activity():
        try:
            r = requests.get(API, timeout=30)
            r.raise_for_status()
            return r.json()
        except Exception as e:
            logging.error(f"Failed to fetch activity: {e}")
            return {"activity": "Relax and take it easy!"}  # Fallback

    @task
    def write_activity_to_file(response):
        filepath = Variable.get("activity_file", default_var="/tmp/activity_log.txt")
        activity = response.get("activity", "No activity found.")
        with open(filepath, "a") as f:
            f.write(f"Today you will: {activity}\r\n")
        return filepath

    @task
    def read_activity_from_file(filepath):
        with open(filepath, "r") as f:
            logging.info(f.read())

    response = get_activity()
    filepath = write_activity_to_file(response)
    read_activity_from_file(filepath)

find_activity()

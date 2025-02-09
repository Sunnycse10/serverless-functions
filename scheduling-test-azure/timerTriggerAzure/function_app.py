import azure.functions as func
import json
from datetime import datetime, timezone
import logging
import requests


app = func.FunctionApp()

@app.timer_trigger(schedule="0 */15 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    url = "https://schedulingtestazure.azurewebsites.net/api/schedulingtestazurefunction"

    # Set headers and payload for the HTTP request
    headers = {
        "X-Scheduler-Trigger-Time": datetime.now(timezone.utc).isoformat()  # Adding trigger time
    }
    payload = {
        "additional_data": "Timer-triggered request"
    }

    try:
        # Send an HTTP POST request to the HTTP trigger
        response = requests.post(url, headers=headers, json=payload)
        logging.info(f"HTTP Trigger Response: {response.status_code} - {response.text}")
    except Exception as e:
        logging.error(f"Error invoking HTTP trigger: {e}")


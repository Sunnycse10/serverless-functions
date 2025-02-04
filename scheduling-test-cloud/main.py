import functions_framework
import logging
from datetime import datetime, timezone
import json


@functions_framework.http
def scheduling_test(request):
    """HTTP Cloud Function triggered by Cloud Scheduler."""
    try:
        # Log the current time
        invocation_time = datetime.now(timezone.utc).isoformat()
        
        # Log any payload sent by the scheduler
        request_data = request.get_json(silent=True) or {}

        log_entry = {
            "message": "Function invoked successfully",
            "invocation_time": invocation_time,
            "scheduler_payload": request_data
        }
        print(log_entry)

        logging.info(json.dumps(log_entry))

        # Return the log entry as a response
        return json.dumps(log_entry), 200

    except Exception as e:
        return json.dumps({"error": str(e)}), 500

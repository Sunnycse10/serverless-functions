import azure.functions as func
import json
from datetime import datetime, timezone
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="schedulingTestAzureFunction")
def schedulingTestAzureFunction(req: func.HttpRequest) -> func.HttpResponse:
    try:
        invocation_time = datetime.now(timezone.utc).isoformat()
        try:
            request_data = req.get_json()  # This will raise an error if the body is not valid JSON
        except ValueError:
            request_data = {}
        log_entry = {
            "message": "Function invoked successfully",
            "invocation_time": invocation_time,
            "scheduler_payload": request_data
        }
        
        print(json.dumps(log_entry))
        return func.HttpResponse(
            json.dumps(log_entry),
            status_code=200,
            mimetype="application/json"
        )
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )
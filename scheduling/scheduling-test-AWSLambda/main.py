import json
from datetime import datetime, timezone
import logging

def lambda_handler(event, context):
    try:
        # Get the current UTC time
        invocation_time = datetime.now(timezone.utc).isoformat()
        
        # Try to parse the JSON body of the request
        request_data = {}
        if 'body' in event:
            try:
                request_data = json.loads(event['body'])  # This assumes the body is JSON
            except ValueError:
                request_data = {}
        
        # Create the log entry
        log_entry = {
            "message": "Function invoked successfully",
            "invocation_time": invocation_time,
            "scheduler_payload": request_data
        }
        
        print(json.dumps(log_entry))
        
        # Return the HTTP response
        return {
            'statusCode': 200,
            'body': json.dumps(log_entry),
            'headers': {
                'Content-Type': 'application/json'
            }
        }

    except Exception as e:
        # Handle any errors
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
import json
import math

def factorials(limit):
    """Compute factorials of numbers up to the limit."""
    result = {}
    for i in range(1, limit + 1):
        result[i] = math.factorial(i)
    return result

def lambda_handler(event, context):
    """AWS Lambda handler for computing factorials up to a given limit."""
    try:
        # Parse 'limit' from query parameters or body
        limit = event.get("queryStringParameters", {}).get("limit")
        if not limit:
            try:
                body = json.loads(event.get("body", "{}"))
                limit = body.get("limit", 10)
            except (ValueError, TypeError):
                limit = 10  # Default limit if no input is provided

        # Ensure limit is a valid integer
        limit = int(limit)
        if limit <= 0:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Invalid limit provided"}),
                "headers": {"Content-Type": "application/json"},
            }

        # Perform the computation
        factorials_result = factorials(limit)

        return {
            "statusCode": 200,
            "body": json.dumps(factorials_result),
            "headers": {"Content-Type": "application/json"},
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": str(e)}),
            "headers": {"Content-Type": "application/json"},
        }
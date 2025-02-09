import azure.functions as func
import logging
import math
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


def factorials(limit):
    """Compute factorials of numbers up to the limit."""
    result = {}
    for i in range(1, limit + 1):
        result[i] = math.factorial(i)
    return result

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    """HTTP Trigger Function for computing factorials up to a given limit."""
    try:
        # Parse 'limit' from query parameters or request body
        limit = req.params.get("limit")
        if not limit:
            try:
                req_body = req.get_json()
                limit = req_body.get("limit", 10)
            except (ValueError, TypeError):
                limit = 10  # Default limit if no input is provided

        # Ensure limit is a valid integer
        limit = int(limit)
        if limit <= 0:
            return func.HttpResponse(
                json.dumps({"message": "Invalid limit provided"}),
                status_code=400,
                mimetype="application/json",
            )

        # Perform the computation
        factorials_result = factorials(limit)

        return func.HttpResponse(
            json.dumps(factorials_result),
            status_code=200,
            mimetype="application/json",
        )

    except Exception as e:
        return func.HttpResponse(
            json.dumps({"message": str(e)}),
            status_code=500,
            mimetype="application/json",
        )
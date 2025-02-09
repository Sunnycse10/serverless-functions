import functions_framework
import math
import json

def factorials(limit):
    """Compute factorials of numbers up to the limit."""
    result = {}
    for i in range(1, limit + 1):
        result[i] = math.factorial(i)
    return result

@functions_framework.http
def factorial_trigger(request):
    """HTTP Cloud Function for computing factorials up to a given limit."""
    try:
        # Parse 'limit' from query parameters or request body
        limit = request.args.get("limit")
        if not limit:
            try:
                req_body = request.get_json()
                limit = req_body.get("limit", 10)
            except (ValueError, TypeError):
                limit = 10  # Default limit if no input is provided

        # Ensure limit is a valid integer
        limit = int(limit)
        if limit <= 0:
            return json.dumps({"message": "Invalid limit provided"}), 400

        # Perform the computation
        factorials_result = factorials(limit)

        return json.dumps(factorials_result), 200

    except Exception as e:
        return json.dumps({"message": str(e)}), 500

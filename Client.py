import json
import time
import uuid

from PRNG import REQUESTS, RESPONSES, write_json


class PRNGClient:
    def __init__(self, user_id):
        if not isinstance(user_id, str) or not user_id.strip():
            raise ValueError("user_id must be a non-empty string.")

        # Remember the user ID for all future requests.
        self.user_id = user_id

        REQUESTS.mkdir(exist_ok=True)
        RESPONSES.mkdir(exist_ok=True)

    def generate(self, category):
        if not isinstance(category, str) or not category.strip():
            raise ValueError("category must be a non-empty string.")

        # Give every request a unique filename.
        request_id = uuid.uuid4().hex
        request_file = REQUESTS / f"{request_id}.json"
        response_file = RESPONSES / f"{request_id}.json"

        write_json(request_file, {
            "user_id": self.user_id,
            "category": category
        })

        # Wait for the response belonging to this request.
        deadline = time.monotonic() + 60

        while not response_file.exists():
            if time.monotonic() >= deadline:
                raise TimeoutError(
                    f"No response within 60 seconds. "
                    f"Request ID: {request_id}"
                )

            time.sleep(0.2)

        response = json.loads(
            response_file.read_text(encoding="utf-8")
        )

        # Remove the response after reading it.
        response_file.unlink()

        if "error" in response:
            raise ValueError(response["error"])

        return response["number"]
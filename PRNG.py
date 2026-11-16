import json
import random
import time
import uuid
from pathlib import Path
# Create the `requests` and `responses` folders and the `results.json` file in the same directory as `PRNG.py` if they don’t already exist.
BASE = Path(__file__).resolve().parent
REQUESTS = BASE / "requests"
RESPONSES = BASE / "responses"
RESULTS = BASE / "results.json"


def write_json(path, data):
    # Publish the file only after writing is complete.
    temp = path.with_name(path.name + "." + uuid.uuid4().hex + ".tmp")
    temp.write_text(
        json.dumps(data, indent=4, ensure_ascii=False),
        encoding="utf-8"
    )
    temp.replace(path)


def main():
    REQUESTS.mkdir(exist_ok=True)
    RESPONSES.mkdir(exist_ok=True)

    # Load the results saved during previous runs.
    if RESULTS.exists():
        results = json.loads(RESULTS.read_text(encoding="utf-8"))
    else:
        results = {}

    print("PRNG service is running.")

    while True:
        for request_file in REQUESTS.glob("*.json"):
            response_file = RESPONSES / request_file.name

            try:
                request = json.loads(
                    request_file.read_text(encoding="utf-8")
                )

                user_id = request["user_id"]
                category = request["category"]

                if (
                    not isinstance(user_id, str)
                    or not user_id.strip()
                    or not isinstance(category, str)
                    or not category.strip()
                ):
                    raise ValueError(
                        "user_id and category must be non-empty strings."
                    )

            except (ValueError, KeyError, TypeError) as error:
                write_json(response_file, {"error": str(error)})
                request_file.unlink()
                continue

            number = random.randint(1, 10)

            # Keep each user's data separate.
            if user_id not in results:
                results[user_id] = {}

            # Update only the requested category for this user.
            results[user_id][category] = number
            write_json(RESULTS, results)

            # Match the response to its original request.
            write_json(response_file, {
                "user_id": user_id,
                "category": category,
                "number": number
            })

            request_file.unlink()

        time.sleep(0.2)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPRNG service stopped.")

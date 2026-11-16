# PRNG Microservice

This microservice generates a random integer from 1 to 10. It uses JSON files to communicate with the main program and saves the latest result for each user and category.

## Requirements

Python 3. No additional packages are needed.

## How to Run

Keep all three Python files in the same folder.

First, run python3 PRNG.py
    
Leave it running, then run python3 main.py

## How to Use

Start `PRNG.py` before making requests. You can adapt the example
in `main.py` to use the microservice in your own program:

```python
from Client import PRNGClient

prng = PRNGClient("your_user_id")

# Send a request and wait for the returned number.
number = prng.generate("category")

# Use the received number.
print("Received:", number)
```

The client automatically includes the user ID in each request.
You can reuse the same client for additional calls.

### Requesting Data

Calling `generate(category)` writes a JSON request containing
the user ID and category to the `requests/` folder. Each request
has a unique filename.

### Receiving Data

The microservice processes the request and writes a JSON response
to the `responses/` folder using the same filename.

The same `generate()` call waits for the response, reads it, and
returns the random number. No separate receive call is needed.
If no response arrives within 60 seconds, it raises a `TimeoutError`.

## Files

- `PRNG.py`: Runs the microservice.
- `Client.py`: Provides the client class for sending requests.
- `main.py`: Shows example calls.
- `requests/`: Stores pending requests.
- `responses/`: Stores responses waiting to be read.
- `results.json`: Saves the latest result for each user and category.

The folders and results file are created automatically when needed.

## Saved Results

Results are organized by user and category:

 {
    "Luoton": {
        "meal": 1
    },
    "Robert": {
        "dashboard": 3
    },
    "Alexander": {
        "textadv": 4
    }
}

A new request replaces only that user's result in the requested category. Other results remain unchanged. The same random number may appear again.

## UML
<img width="1900" height="1830" alt="image" src="https://github.com/user-attachments/assets/ed7b5c62-3d5c-467e-8b4d-037fcbc7deaf" />


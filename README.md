# PRNG Microservice

This microservice generates a random integer from 1 to 10. It uses JSON files to communicate with the main program and saves the latest result for each user and category.

## Requirements

Python 3. No additional packages are needed.

## How to Run

Keep all three Python files in the same folder.

First, run python3 PRNG.py
    
Leave it running, then run python3 main.py

## How to Use
You can adapt the example in main.py to call PRNG from your own program. Simply import the client, create a client with your user ID, and call generate() with a category:

from Client import PRNGClient

prng = PRNGClient("your_user_id")
number = prng.generate("category")

Reuse the same client whenever you need another random number. Make sure PRNG.py is running before making calls.


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

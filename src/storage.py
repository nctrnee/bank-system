from pathlib import Path  # Modern way of working with file/folders
import json

# Path object: json/accounts.json
# Like an address
PATH = Path("json") / "accounts.json"


def load_data():
    """Load account data from JSON"""
   
    with PATH.open("r") as file:
        return json.load(file)


def dump_data(data):
    """Dump account data to JSON"""
    # Checks if json/ exist. If not, create
    PATH.parent.mkdir(parents=True, exist_ok=True)

    with PATH.open("w") as file:
        json.dump(data, file, indent=4)

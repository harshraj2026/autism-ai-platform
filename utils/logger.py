import json
import os
from datetime import datetime

def save_log(filename, data):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filepath = os.path.join(folder, f"{timestamp}_{filename}")

    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)



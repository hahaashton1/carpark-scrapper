import requests
import json
from datetime import datetime
import pandas as pd
import os

save_path = './HDB'
status = 0

while status != 200:
    response = requests.get("https://api.data.gov.sg/v1/transport/carpark-availability")
    status = response.status_code

now = datetime.now().strftime("%d-%m-%Y %H%M%S")

file_name = "Results " + now + ".json"
file_name = os.path.join(save_path,file_name)
text = json.dumps(response.json(), sort_keys=True, indent=4)

with open(file_name, "w") as results_file:
    results_file.write(text)

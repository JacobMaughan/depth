# Description: The json file handler for the python game template
# Created By: Jacob Maughan

import json

def getData(file):
    with open(file, 'r') as file:
        return json.load(file)

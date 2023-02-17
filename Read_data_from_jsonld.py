import json

# Load the JSON-LD file
with open("ontology.jsonld", "r") as f:
    data = json.load(f)

# Iterate over the items in the list
for item in data:
    print(item)

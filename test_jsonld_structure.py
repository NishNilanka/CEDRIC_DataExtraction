import json

# Load the JSON-LD file
with open("ontology.jsonld", "r") as f:
    data = json.load(f)

# Check the structure of the data
print(type(data))
if "@graph" in data:
    print(type(data["@graph"]))
else:
    print("No @graph key found")

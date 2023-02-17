import rdflib


g = rdflib.Graph()
g.parse("CEDRIC.owl", format="xml")

# Serialize the graph as JSON-LD
jsonld = g.serialize(format='json-ld')

# Write the JSON-LD to a file
with open("ontology.jsonld", "wb") as f:
    f.write(jsonld.encode('utf-8'))

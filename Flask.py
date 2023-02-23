from flask import Flask, jsonify
from rdflib import Graph, Namespace, RDF

# Define the namespaces
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")

app = Flask(__name__)

g = Graph()
g.parse("CEDRIC_2.owl")

def read_owl_file():
    for s, p, o in g.triples((None, RDF.type, OWL.NamedIndividual)):
        if str(s).startswith("http://www.semanticweb.org/CEDRIC/"):
            # Check if the subject is a DataElement element
            if (s, RDF.type, Namespace("http://www.semanticweb.org/CEDRIC/").DataElement) in g:
                # Get the value of the attribute element
                attribute = str(g.value(s, Namespace("http://www.semanticweb.org/CEDRIC/").attribute))

                # Get the value of the comments element
                comments = str(g.value(s, Namespace("http://www.semanticweb.org/CEDRIC/").comments))

                table = str(g.value(s, Namespace("http://www.semanticweb.org/CEDRIC/").table))


@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'name': 'John', 'age': 30, 'city': 'New York'}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

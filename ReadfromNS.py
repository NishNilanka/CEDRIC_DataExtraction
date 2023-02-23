import json

from rdflib import Graph, Namespace, RDF

# Define the namespaces
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")

# Load the OWL file into a graph
g = Graph()
g.parse("CEDRIC_2.owl")

# Iterate through all the DataElement elements in the graph
tables = []


def check_tables(tablename):
    count = 0
    for x in tables:
        if x[0] == tablename:
            return count
        count += 1
    return -1


def check_null(text):
    if text != 'None':
        return text.split('/')[4]
    else:
        return text


for s, p, o in g.triples((None, RDF.type, OWL.NamedIndividual)):
    if str(s).startswith("http://www.semanticweb.org/CEDRIC/"):
        # Check if the subject is a DataElement element
        if (s, RDF.type, Namespace("http://www.semanticweb.org/CEDRIC/").DataElement) in g:
            # Get the value of the attribute element
            attribute = str(g.value(s, Namespace("http://www.semanticweb.org/CEDRIC/").attribute))

            # Get the value of the comments element
            comments = str(g.value(s, Namespace("http://www.semanticweb.org/CEDRIC/").comments))
            datatype = str(g.value(s, Namespace("http://www.semanticweb.org/CEDRIC/").hasDataType))
            datatype = check_null(datatype)
            table = str(g.value(s, Namespace("http://www.semanticweb.org/CEDRIC/").table))
            possibleRowDataManipulationTechnique = \
                str(g.value(s, Namespace(
                    "http://www.semanticweb.org/CEDRIC/").possibleRowDataManipulationTechnique))
            possibleRowDataManipulationTechnique = check_null(possibleRowDataManipulationTechnique)
            possiblePopulationManipulationTechnique = str(g.value(s, Namespace(
                "http://www.semanticweb.org/CEDRIC/").possiblePopulationManipulationTechnique))
            possiblePopulationManipulationTechnique = check_null(possiblePopulationManipulationTechnique)
            #print(possiblePopulationManipulationTechnique)
            hasPrivacyLevel = \
                str(g.value(s, Namespace("http://www.semanticweb.org/CEDRIC/").hasPrivacyLevel))
            hasPrivacyLevel = check_null(hasPrivacyLevel)
            # tables[table] = [attribute, possibleRowDataManipulationTechnique, possiblePopulationManipulationTechnique, hasPrivacyLevel]
            # Do something with the attribute and comments values
            data = {
                "attribute": attribute,
                "dataType":datatype,
                "dSensitivity": hasPrivacyLevel,
                "filterRule": possibleRowDataManipulationTechnique
            }

            table_check = check_tables(table)
            if table_check == -1:
                tables.append([table, data])
            else:
                tables[table_check].append(data)

#print(tables)
with open('data.json', 'w') as f:
    #Write the dictionary to the file in JSON format
    json.dump(tables, f)

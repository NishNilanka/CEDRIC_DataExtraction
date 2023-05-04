from rdflib import Graph

# create a Graph object
g = Graph()

# parse the TTL file
g.parse("my_ontology.ttl", format="ttl")

# iterate through the triplets and print them
# Sort the triples by subject, predicate, object
triples = sorted(g, key=lambda t: (str(t[0]), str(t[1]), str(t[2])))

count = 0
for subj, pred, obj in triples:
    # Remove the prefix from the subject and object
    if str(subj).startswith("http://www.semanticweb.org/CEDRIC/OMOP"):
        subject_without_prefix = subj.replace("http://www.semanticweb.org/CEDRIC/OMOP/", "")
        if (str(obj).startswith("http://www.semanticweb.org/CEDRIC/OMOP")):
            object_without_prefix = obj.replace("http://www.semanticweb.org/CEDRIC/OMOP/", "")
            if (str(pred).__contains__("subPropertyOf")):
                print(subject_without_prefix, pred, object_without_prefix)
                count += 1

print(count)

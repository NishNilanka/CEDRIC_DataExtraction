from rdflib import Graph

# create a graph and load some data
g = Graph()
g.parse("CEDRIC.owl", format="xml")

# get the namespace manager
ns_mgr = g.namespace_manager

# find the namespace for the default prefix
ontology_ns = ns_mgr.store.namespace("")
print(ontology_ns)

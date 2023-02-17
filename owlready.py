from owlready2 import get_ontology

ontology = get_ontology("CEDRIC.owl").load()

for cls in ontology.classes():
    instance = cls()
    print("Class name: ", cls)
    for prop in instance.get_properties():
        print("\tProperty: ", prop)

for ind in ontology.individuals():
    print("Individual name: ", ind)
    for prop in ind.get_properties():
        print("\tProperty: ", prop)

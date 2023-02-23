# This is a sample Python script.

import rdflib
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    g = rdflib.Graph()
    g.parse("CEDRIC.owl", format="xml")
    print("Hi")
    qres = g.query(
    """SELECT ?predicate ?object
       WHERE {
          <http://www.semanticweb.org/CEDRIC/gender_source_concept_id> ?predicate ?object .
       }""")
    count = 0
    for row in qres:
        count += 1
        print(row)
    print(count)
    #for s, p, o in g:
    #    print(s, p, o)
        #print(s[34:])
        #print(p)  # Press Ctrl+F8 to toggle the breakpoint.


# Load the .owl file into an RDF graph




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

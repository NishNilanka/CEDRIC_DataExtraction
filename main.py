# This is a sample Python script.

import rdflib
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    g = rdflib.Graph()
    g.parse("CEDRIC.owl", format="xml")
    #print(g)
    # Iterate through the triples in the graph
    for s, p, o in g:
        print(s, p, o)
        #print(s[34:])
        #print(p)  # Press Ctrl+F8 to toggle the breakpoint.


# Load the .owl file into an RDF graph




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

package com.example;

import java.io.File;

import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.model.*;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        OWLOntologyManager ontologyManager = OWLManager.createOWLOntologyManager();
        File file = new File("my_ontology.ttl");
        OWLOntology ontology = null;
        try {
            ontology = ontologyManager.loadOntologyFromOntologyDocument(file);
        } catch (OWLOntologyCreationException e) {
            e.printStackTrace();
        }
        
        // Print some information about the ontology
        System.out.println("Loaded ontology: " + ontology.getOntologyID().getOntologyIRI().get());
        System.out.println("Axiom count: " + ontology.getAxiomCount());
        g
        // Iterate over the datatype properties in the ontology and print their names
        for (OWLDataProperty prop : ontology.getDataPropertiesInSignature()) {
            System.out.println("Datatype Property: " + prop.getIRI().getFragment());
        }
    }
}

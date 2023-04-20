package com.example;

import java.io.File;

import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.model.*;

public class OwlParser {

    public static void main( String[] args )
    {
        OWLOntologyManager ontologyManager = OWLManager.createOWLOntologyManager();
        File file = new File("my_ontology.owl");
        OWLOntology ontology = null;
        try {
            ontology = ontologyManager.loadOntologyFromOntologyDocument(file);
        } catch (OWLOntologyCreationException e) {
            e.printStackTrace();
        }
        
        // Print some information about the ontology
        System.out.println("Loaded ontology: " + ontology.getOntologyID().getOntologyIRI().get());
        System.out.println("Axiom count: " + ontology.getAxiomCount());
        
        // Iterate over the datatype properties in the ontology and print their names
        for (OWLDataProperty prop : ontology.getDataPropertiesInSignature()) {
            System.out.println("Datatype Property: " + prop.getIRI().getFragment());
            for (OWLClass cls : ontology.getClassesInSignature()) {
                for (OWLOntology o : ontologyManager.getOntologies()) {
                    for (OWLDataPropertyDomainAxiom ax : o.getAxioms(AxiomType.DATA_PROPERTY_DOMAIN)) {
                        if (ax.getProperty().equals(prop)) {
                            System.out.println("Domain Class: " + ax.getDomain());
                            break;
                        }
                    }
                }
            }
        }
    }
}

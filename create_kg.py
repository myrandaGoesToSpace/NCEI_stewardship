import kglab
import pyvis.network
import rdflib
import pandas as pd

def main():

    kg = kglab.KnowledgeGraph().load_rdf("stewardship_docs_rdf.xml", format="xml")

    subgraph = kglab.SubgraphTensor(kg)
    pyvis_graph = subgraph.build_pyvis_graph()

    pyvis_graph.force_atlas_2based()
    pyvis_graph.show("tmp.stewardship.html")

main()

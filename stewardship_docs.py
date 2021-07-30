
import kglab
import rdflib
import pyvis.network

# Description: creates a graph of NCEI Stewardship Documentation, as described by https://tables.area120.google.com/u/0/workspace/aO2JdKpLi0E8OCducMd4iq/table/ahtQ0Tw_c07eU8v3hAC_EI
# Purpose: to provide resources for new employees to understand structures and processes within NCEI
# Author: Myranda Uselton (myranda.uselton@noaa.gov)

def main():
    pyvis_graph = pyvis.network.Network()

    pyvis_graph.add_node(0, label = "NCEI-CO", title = "NCEI location in Boulder, CO", color="blue", size=9)
    pyvis_graph.add_node(1, label = "Archive Ecosystem Outline", title="Description", color = "orange", size = 7)
    pyvis_graph.add_node(2, label = "Stewardship Documentation WG", title = "Description", color = "green", size = 5)
    pyvis_graph.add_node(3, label = "NCEI-NC", title = "NCEI location in Asheville, NC", color = "blue", size=9)
    pyvis_graph.add_node(4, label = "Example Person", title = "Example Person", color = "red", size = 5)

    pyvis_graph.add_edge(0, 1, label = "uses documentation")
    pyvis_graph.add_edge(1, 4, label = "associated with SME")
    pyvis_graph.add_edge(1, 2, label = "has subject tag")
    pyvis_graph.add_edge(3, 1, label = "uses documentation")
    pyvis_graph.add_edge(4, 3, label = "duty station")

    pyvis_graph.force_atlas_2based()
    pyvis_graph.show("tmp.stewardship.html")

main()

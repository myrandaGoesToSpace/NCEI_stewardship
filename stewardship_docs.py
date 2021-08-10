
import kglab
import rdflib
import pyvis.network
import pandas as pd

# Description: creates a graph of NCEI Stewardship Documentation, as described by https://tables.area120.google.com/u/0/workspace/aO2JdKpLi0E8OCducMd4iq/table/ahtQ0Tw_c07eU8v3hAC_EI
# Purpose: to provide resources for new employees to understand structures and processes within NCEI
# Author: Myranda Uselton (myranda.uselton@noaa.gov)
def xml_replace(string):
    return str(string).replace("&", "&amp;")

def get_tags(subject_string, open_tag, close_tag):
    subject_list = subject_string.split(",")
    fo_string = ""

    for subject in subject_list:
        fo_string = fo_string + open_tag + subject + close_tag
    return xml_replace(fo_string)

def main():

    # TEST
    ''' 
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
    '''

    # import csv
    docs_csv = pd.read_csv("./stewardship_docs.csv")

    # TEST
    print(docs_csv)
    print(type(docs_csv["Subject Matter Tags"][1].split(",")))

    # convert CSV to XML RDF
    fo = open("stewardship_docs_rdf.xml","w")

    fo.write("<?xml version='1.0' encoding='UTF-8' ?>")
    fo.write("<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#' xmlns:schema='https://schema.org/' >")

    for i in range(0, len(docs_csv)):
            fo.write("<rdf:Description>")
    
            # Add title, strip of special characters
            title_string = "<rdf:title>" + xml_replace(str(docs_csv["File Title"][i])) + "</rdf:title\n>"
            fo.write(title_string)

            link_string = "<a href='" + xml_replace(str(docs_csv["Link"][i])) + "'/>\n"
            fo.write(link_string)

            # Subject Matter Tags
            fo.write(get_tags(str(docs_csv["Subject Matter Tags"][i]), "<rdf:Subject>", "</rdf:Subject>\n"))

            # Infrastructure Tags
            fo.write(get_tags(str(docs_csv["Infrastructure Tags"][i]), "<rdf:InfrastructureTag>", "</rdf:InfrastructureTag>\n")) 
                    
            # Geography Tags
            fo.write(get_tags(str(docs_csv["Geography Tags"][i]), "<rdf:Geography>", "</rdf:Geography>\n"))

            # SME
            fo.write(get_tags(str(docs_csv["Subject Matter Experts (SMEs)"][i]), "<rdf:SME>", "</rdf:SME>\n"))

            fo.write("</rdf:Description>\n")

    fo.write("</rdf:RDF>")

    fo.close()

main()

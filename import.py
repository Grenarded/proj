import json 
import xml.etree.ElementTree as ET

#Define 'Way' object
class Way:
    def __init__(self, way_id, nodes):
        self.way_id = way_id
        self.nodes = nodes

#Define 'Node' object
class Node:
    def __init__(self, node_id, lat, lon):
        self.node_id = node_id
        self.lat = lat
        self.lon = lon

#Define 'Bot' object
class Bot:
    def __init__(self, location, capacity):
        self.location = location
        self.capacity = capacity

#Define 'Package' object
class Package:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

#Specify file path
file_path = 'TA1.json'

#Open the file in read mode
with open(file_path, 'r') as file:
    #Load JSON file
    data = json.load(file)

#Access the 'bots' list
bots_list = data['bots']

#Access the 'packages' list
packages_list = data['packages']

#Create instances of 'Bot' and 'Package' classes
bots = [Bot(bot['location'], bot['capacity']) for bot in bots_list]
packages = [Package(package['source'], package['destination']) for package in packages_list]

# Specify the path to XML file
xml_file_path = 'TA1.xml'

# Parse the XML file
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Create lists to store Node and Way objects
nodes = []
ways = []

# Iterate over elements in the XML tree
for element in root:
    if element.tag == 'node':
        # Extract node attributes
        node_id = int(element.attrib['id'])
        lat = float(element.find('lat').text)
        lon = float(element.find('lon').text)

        # Create Node object and add to the list
        nodes.append(Node(node_id, lat, lon))

    elif element.tag == 'way':
        # Extract way attributes
        way_id = int(element.attrib['id'])
        
        # Extract node references within the way
        node_references = [int(node.text) for node in element.findall('node')]

        # Create Way object and add to the list
        ways.append(Way(way_id, node_references))

# TEMPORARY #
for bot in bots:
    print(f"Bot at location {bot.location} with capacity {bot.capacity}")

for package in packages:
    print(f"Package from {package.source} to {package.destination}")

for node in nodes:
    print(f"Node {node.node_id}: Lat {node.lat}, Lon {node.lon}")

for way in ways:
    print(f"Way {way.way_id}: Nodes {way.nodes}")
# # # #

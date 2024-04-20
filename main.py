"""
Title: Fortigate Address Object Adder
Author: Eric Caverly
Date: 04/19/2024
"""

from fortigate_api import FortiGateAPI as fg
import csv
import json
import argparse

cfg_path = "./config.json"

# Parse arguments for more usability
parser = argparse.ArgumentParser(prog='Fortigate Address Adder')
parser.add_argument('-d', '--delete', action='store_true', help="delete objects in the CSV from the Fortigate")
parser.add_argument('-v', '--verbose', action='store_true', help="print data to console while adding/updating objects")
parser.add_argument('-c', '--config', help="specify a custom config file location")
args = parser.parse_args()

# Get data from arguments
delete = args.delete
verbose = args.verbose
if(args.config):
    cfg_path = args.config


# Open the Config file and parse it as JSON
with open(cfg_path) as config_file:
    contents = config_file.read()
    contents = contents.replace("\n", "").strip()
    config = json.loads(contents)


# Create the API object
api = fg(host=config['fw'], username=config['username'], password=config['password'])


"""
Example Data Structure:


data = {
    "name": "TestOBJ3",
    "obj-type": "ip",
    "subnet": "192.168.2.0 255.255.255.0",
    "type": "ipmask",
    "comment": "Example object"
}
"""

# All elements to be added into the address group
address_list = []

with open(config['filename'], "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Check if we need to delete the address group
    addrGrpExists = len(api.cmdb.firewall.addrgrp.get(name=config["addressObjectName"]))
    if(addrGrpExists and delete):
        response = api.cmdb.firewall.addrgrp.delete(config["addressObjectName"]) 
        print("address_group.delete [%s] - %s" % (config["addressObjectName"], response))


    # Go through each object in the CSV
    for row in csv_reader:
        data = {
            "name": row[1].strip(),
            "obj-type": "ip",
            "comment": row[2].strip(),
            "type": row[0].strip(),
            "color": config["addressColor"],
        }

        # Determine what type of object to create. If more types are required, add them here
        if(row[0].strip() == "fqdn"):
            data["fqdn"] = row[3].strip()
        elif(row[0].strip() == "ipmask"):
            data["subnet"] = row[3].strip()


        # Check if the object already exists
        exists = len(api.cmdb.firewall.address.get(name=data["name"]))
        if(exists):
            # if the object exists, delete if set to delete, otherwise update it with new data
            if(delete):
                response = api.cmdb.firewall.address.delete(data["name"])
                print("address.delete [%s] - %s" % (data["name"], response))
            else:
                if(verbose):
                    print("\n\n")
                    print(data)
                    print("")
                response = api.cmdb.firewall.address.update(data)
                print("address.update [%s] - %s" % (data["name"], response))


        # If the object does not exist, and we are not deleting objects, create it
        elif(not delete):
            if(verbose):
                print("\n\n")
                print(data)
                print("")
            response = api.cmdb.firewall.address.create(data)
            print("address.create [%s] - %s" % (data["name"], response))


        # Append the name of the object so it can be put in the group
        address_list.append({"name": data["name"], "q_origin_key": data["name"]})


if(not delete):
    # Create payload for creating address group with list
    addrGrpData = {
        "name": config["addressObjectName"],
        "member": address_list,
        "color": config["addressGroupColor"],
    }


    # If the group exists, update it. Otherwise create it
    if(verbose):
        print("\n\n")
        print(addrGrpData)
        print("")
    if(addrGrpExists):
        response = api.cmdb.firewall.addrgrp.update(addrGrpData)
        print("address_group.update [%s] - %s" % (addrGrpData["name"], response))
    elif(not delete):
        response = api.cmdb.firewall.addrgrp.create(addrGrpData)
        print("address_group.create [%s] - %s" % (addrGrpData["name"], response))

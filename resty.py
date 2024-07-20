# This will be a template for REST CONF to Cisco ISO-XE platform CSR1000v

import requests
import json
from pprint import pprint

# Replace these variables with your router's details
router_ip = "172.16.1.31"
username = "cisco"
password = "cisco"

# Disable warnings about insecure connections
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

#REST API
base_url = f"https://{router_ip}/restconf"

# Headers
headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json"
}

# GET HOSTNAME
def get_hostname():
    url = f"{base_url}/data/Cisco-IOS-XE-native:native/hostname"
    response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    if response.status_code == 200:
        hostname = response.json()["Cisco-IOS-XE-native:hostname"]
        pprint(f"Hostname: {hostname}")
    else:
        pprint(f"Failed to get hostname. Status code: {response.status_code}")

# GET INTERFACES
def get_interfaces():
    url = f"{base_url}/data/ietf-interfaces:interfaces"
    response = requests.get(url, headers=headers, auth=(username, password), verify=False)
    if response.status_code == 200:
        interfaces = response.json()["ietf-interfaces:interfaces"]["interface"]
        for interface in interfaces:
            pprint(f"Interface: {interface['name']}, Status: {interface['enabled']}")
    else:
        pprint(f"Failed to get interfaces. Status code: {response.status_code}")

# Main function
def main():
    get_hostname()
    get_interfaces()

if __name__ == "__main__":
    main()
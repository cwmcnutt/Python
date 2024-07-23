# fortios api token 371617k0xb4156s719mzc3z78sf4qr


import requests
import json

# Replace these variables with your FortiGate details
fortigate_ip = "172.16.1.1"
username = "cwmcnutt"
password = "371617k0xb4156s719mzc3z78sf4qr"

# Disable warnings about insecure connections
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Base URL for the REST API
base_url = f"https://{fortigate_ip}/api/v2"

# Function to get the system status
def get_system_status():
    url = f"{base_url}/monitor/system/status"
    response = requests.get(url, auth=(username, password), verify=False)
    if response.status_code == 200:
        system_status = response.json()
        print(json.dumps(system_status, indent=4))
    else:
        print(f"Failed to get system status. Status code: {response.status_code}")

# Function to get the firewall policies
def get_firewall_policies():
    url = f"{base_url}/cmdb/firewall/policy"
    response = requests.get(url, auth=(username, password), verify=False)
    if response.status_code == 200:
        policies = response.json()
        print(json.dumps(policies, indent=4))
    else:
        print(f"Failed to get firewall policies. Status code: {response.status_code}")

# Main function
def main():
    get_system_status()
    get_firewall_policies()

if __name__ == "__main__":
    main()

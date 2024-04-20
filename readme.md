# Fortigate IP adder
Written for BAIST students at NAIT to import intune IP addresses from a CSV. Creating a lot of IP address objects is a common enough task that I felt making the script more versatile would be handy. Feel free to use it however you want.

### Fortigate Pre-Requisites
- Somewhat modern version of FortiOS
- Admin account without 2FA

### Python Requirements
```bash
pip install fortigate-api
```

### CMD usage
```
usage: Fortigate Address Adder [-h] [-d] [-v] [-c CONFIG]

options:
  -h, --help            show this help message and exit
  -d, --delete          delete objects in the CSV from the Fortigate
  -v, --verbose         print data to console while adding/updating objects
  -c CONFIG, --config CONFIG
                        specify a custom config file location
```

### Config file
```
{
    "fw": "IPADDRESS/FQDN:PORT", 
    "username": "USERNAME", 
    "password": "PASSWORD", 
    "addressObjectName": "ADDRGRPNAME",
    "filename": "CSV"
}
```

### Data
- Use the data under "intuneips.csv" as a guide, then update the path in your config appropriately.
- Coloumn layout:

| type | name | comment | subnet/fqdn |
| --- | --- | --- | --- |

> Make sure to NOT include coloumn titles!

### API Library

https://github.com/vladimirs-git/fortigate-api/tree/main




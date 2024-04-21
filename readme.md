# Fortigate IP adder
Super simple python script that uses a CSV file to import address objects into a fortigate, then create an address group that contains all addresses. 

You can specify different config files with `-c` to very quickly add multiple CSVs to 1 or more firewalls.

### Fortigate Pre-Requisites
- Somewhat modern version of FortiOS
- Admin account without 2FA

### Python Requirements
```bash
pip install fortigate-api
```

### CMD usage
```
usage: python main.py [-h] [-d] [-v] [-c CONFIG]

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
    "addressColor": COLORID,
    "addressGroupColor": COLORID,
    "addressObjectName": "ADDRGRPNAME",
    "filename": "CSV"
}
```
> Lime green is 13

### Data
- Use the data under "intuneips.csv" as a guide, then update the path in your config appropriately.
- Coloumn layout:

| type | name | comment | subnet/fqdn |
| --- | --- | --- | --- |

> Make sure to NOT include coloumn titles!

### API Library

https://github.com/vladimirs-git/fortigate-api/tree/main




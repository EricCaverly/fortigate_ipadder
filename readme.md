# Fortigate IP adder
- Written for BAIST students at NAIT, but common thing so polished it a bit

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

### API Library

https://github.com/vladimirs-git/fortigate-api/tree/main




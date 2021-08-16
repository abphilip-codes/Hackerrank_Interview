# Bajaj Preliminary Test

import requests
import json
import jsonpath

endpoint = "https://reqres.in/api/users/2"
endpoint="https://prod24.centralindia.logic.azure.com:443/workflows/78d6df0ed1384ee0b7d04918f1a32b85/triggers/request/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Frequest%2Frun&sv=1.0&sig=i6gXuS7-5_fFVf-0u8M4UfymINDULCMifsscfN5cPKM"
# Put request to endpoint 
r = requests.post(endpoint)
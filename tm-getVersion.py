#!/bin/python

'''
This script is meant to demostrate the possibilities of Totemomail REST Admin-API
Not intended to run in production. Only for experimental / Proof of Concept use
Copyright 2020 Toni Feric

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

version 0.01
'''

import requests
from requests.auth import HTTPDigestAuth
import urllib3

# Replace with the correct URL
url = "https://127.0.0.1:8444/api/v1/version"

# Disable TLS certificate mismatch warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

myResponse = requests.get(url, verify=False)
print (myResponse.status_code)

# For successful API call, response code will be 200 (OK)
if(myResponse.ok):

    # Loading the response data into a dict variable
    jData = myResponse.json()

    #print("The response contains {0} properties".format(len(jData)))
    #print("\n")
    for key in jData:
        print key + " : " + jData[key]
    else:
        # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()


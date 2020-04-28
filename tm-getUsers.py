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
#import json
import pprint
import urllib3
import getpass

# Replace with the correct URL
url_base = "https://127.0.0.1:8444/api/v1"
url_func = "/user"
api_params = {'userType': 'internal', 'limit': '100'}
api_response = []

def get_credentials_from_user():
    user = raw_input("Username: ")
    pw = getpass.getpass("Password for " + user + ":")
    return (user, pw)

def get_resonse_from_api(url_base, url_func, api_params, user, pw):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    api_response = requests.get(
                 url_base + url_func,
                 verify=False,
                 headers={'Accept': 'application/json'},
                 auth=(user, pw),
                 params=api_params)
    return api_response

def json_pretty_print(blob_json):
    #print "PrettyPrint:"
    #print(json.dumps(json.loads(blob_json), indent=2))
    pp = pprint.PrettyPrinter(indent = 4)
    pp.pprint(blob_json)
    #print "After PrettyPrint"

def request_status(blob):
    if(blob.ok):
        return True
    else:
        api_response.raise_for_status()
        return False

def json_ize(blob):
    return blob.json()

def json_select_dataset(blob):
    # Loading the response data into a dict variable
    jData = api_response.json()
    #print str(jData)

    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for dataset in jData:
        for key in dataset:
            #print str(key) + ": " + str(dataset[key])
            i = 1

(user, pw) = get_credentials_from_user()
blob = get_resonse_from_api(url_base, url_func, api_params, user, pw)
blob_json = json_ize(blob)

if(request_status(blob)):
     json_pretty_print(blob_json)


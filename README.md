# totemomail-api
The scripts in this repository are meant to demonstrate some of Totemomail's automation capabilities using REST API.  
These scripts are meant for Proof of Concept and are not intended to run in a productive environment.  
As such, they could be used as a starting point to build own automation scripts.  

Professional services for further customizations can be aquired through Belsoft Collaboration AG at  
https://belsoft-collaboration.ch/totemo/  

# Usage
These scripts are inteded to run on localhost (i.e. the operating system where Totemomail runs), but they could be changed to run from remote.  

## Requirements
On Totemomail, the Admin REST API needs to be enabled, as it is disabled by default.  
Login to the Totemomail Administration GUI as administrator, go to "Settings - Modules" and change the value of "totemo.modules.adminapi.enabled" to "true". Apply changes and restart Totemomail. The Admin REST API should not be listening on Port 8444.  
If the Admin REST API needs to be accessed from remote (e.g. an administrator's browser), the local firewall and zone firewall would have to allow TCP port 8444.  

## Scripts
These scripts are written in Python 2.* and may not run with Python 3.*.  

## Setting up test
Copy the scripts to a suitable host, e.g. to the Totemomail host itself.  
```chmod ug+x tm*.py```  
Run one of the scripts locally.  
  

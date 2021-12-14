# Request Header Spy
put it in azure and get as request response a json with your request headers
or host it any other way -

## Requirements
you need 
* flask

## Azure installation
I used the visualStudio Code tutorial: 
https://docs.microsoft.com/en-us/azure/python/tutorial-deploy-app-service-on-linux-01

In addition I also created a azure-pipeline to build an artifact that can easily be deployed

### Configuration
in your AppService under configuration->General Settings add the Startup Command: 
`gunicorn --bind=0.0.0.0 --workers=4 startup:app`
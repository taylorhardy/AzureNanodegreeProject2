import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import ssl
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = os.environ['MyDbConnection']
        client = pymongo.MongoClient(url, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
        database = client['azurenanodegreecosmodbproject2']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)


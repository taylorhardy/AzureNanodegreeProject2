import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from pymongo.errors import ConnectionFailure
import ssl 
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = os.environ['MyDbConnection']
        client = pymongo.MongoClient(url, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
        database = client['azurenanodegreecosmodbproject2']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except ConnectionFailure as e:
        logging.info(e)
        return func.HttpResponse("Bad request.", status_code=400)
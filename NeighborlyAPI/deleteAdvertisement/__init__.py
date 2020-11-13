import azure.functions as func
import pymongo
from bson.objectid import ObjectId
import ssl 
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = os.environ['MyDbConnection']
            client = pymongo.MongoClient(url, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
            database = client['azurenanodegreecosmodbproject2']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)

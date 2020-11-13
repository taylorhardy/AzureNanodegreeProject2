import azure.functions as func
import pymongo
import ssl 

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://azurenanodegreecosmodbproject2:zcg0hrwtpsvqVB8z1FBkOQtMYnYmYU6raGF9yYrQg4fp2x90Hx7aY5tcyJu3GsQCYTVZdDLYucABUtGkvA7auA==@azurenanodegreecosmodbproject2.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@azurenanodegreecosmodbproject2@"
            client = pymongo.MongoClient(url, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
            database = client['azurenanodegreecosmodbproject2']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )
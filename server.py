
import json
from flask import Flask, Response, request
from service import createSecretService, getSecretService
from dotenv import load_dotenv
from db import init
import os

app = Flask(__name__)
load_dotenv(".env")
envVariables = dict(os.environ)

@app.post("/api/v1/secret")
def createSecretEndpoint():
    data = json.loads(request.data.decode()) #This is a dictionary. 
    try:
        link = createSecretService.create_secret_dao(data, envVariables)
        return Response(link, status=200, mimetype='text/html')
    except Exception as e:
        return Response(str(e), status=405, mimetype='text/html')  

@app.post("/api/v1/getSecret")
def getSecretByHash():
    data : dict = json.loads(request.data.decode())
    try:
        secret = getSecretService.get_secret_by_hash(data.get("hash"), envVariables)
        return Response(json.dumps(secret), status=200, mimetype='application/json')
    except Exception as e:
        return Response(str(e), status=404, mimetype='application/json')
    
@app.post("/api/v1/init")
def init_db():
    try:
        init(envVariables)
        return Response("Init A-OK!", status=200, mimetype='text/html')
    except Exception as e:
        return Response(str(e), status=400, mimetype='application/json')

if(__name__ == '__main__'):
    app.run(debug=True, port=envVariables.get("PORT",5000))
    init(envVariables)

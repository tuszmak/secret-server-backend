import json
import os
from dotenv import load_dotenv
from flask import Flask, Response, request
from service import create_secret_service, get_secret_service
from db import init

app = Flask(__name__)
load_dotenv(".env")
envVariables = dict(os.environ)

@app.post("/api/v1/secret")
def create_secret_endpoint():
    """Create secret from frontend data"""
    data = json.loads(request.data.decode()) #This is a dictionary. 
    try:
        link = create_secret_service.create_secret_dao(data, envVariables)
        return Response(link, status=200, mimetype='text/html')
    except Exception as e:
        return Response(str(e), status=405, mimetype='text/html')  

@app.get("/api/v1/secret/<hash>")
def get_secret_by_hash(hash):
    """Get secret from database by hash"""
    try:
        secret = get_secret_service.get_secret_by_hash(hash, envVariables)
        return Response(json.dumps(secret), status=200, mimetype='application/json')
    except Exception as e:
        return Response(str(e), status=404, mimetype='application/json')    
@app.get("/api/v1/init")
def init_db():
    """Initialize database table"""
    try:
        init(envVariables)
        return Response("Init A-OK!", status=200, mimetype='text/html')
    except Exception as e:
        return Response(str(e), status=400, mimetype='application/json')

if(__name__ == '__main__'):
    app.run(debug=True, port=envVariables.get("PORT",5000))
    init(envVariables)

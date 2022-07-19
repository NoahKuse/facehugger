"""
Test implementation of a Restful API
"""
from flask import Flask
from flask_restful import Api, Resource
import os

app = Flask(__name__)

api =   Api(app)

class HelloWorld(Resource):
    """
    Testclass
    """
    def get(self):
        """
        Getter for hello world
        """
        data={"data":"Hello World"}
        return data

api.add_resource(HelloWorld,'/hello')

if __name__=='__main__':
    cfg_port = os.getenv('PORT', 5000)


    app.run(host="0.0.0.0", port=cfg_port)#, debug=True)

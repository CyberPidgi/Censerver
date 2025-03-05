# Importing flask module in the project is mandatory
# Apipn object of Flask class is our WSGI application.
from flask import Flask, redirect, url_for, request, Response, jsonify
from flask_cors import CORS, cross_origin

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
@cross_origin()
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'


@app.route('/test', methods=['GET'])
@cross_origin()
def test():
    return jsonify({'message': 'Hello World'}) # return JSON response

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
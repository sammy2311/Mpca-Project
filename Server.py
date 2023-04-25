
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, jsonify
import json
import Db

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def get_variables():
    variable = request.json
    print(variable)
    print("Recieved ID", variable['fingerid'])
    return(Db.update(variable['price'], {'fingerid':variable['fingerid']}))



if __name__ == '__main__':
    app.run()

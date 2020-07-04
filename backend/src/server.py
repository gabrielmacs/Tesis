from flask import Flask, jsonify, request
from flask_cors import CORS

from bson import ObjectId

# Instantiation
app = Flask(__name__)

# Settings
CORS(app)


# Routes
@app.route('/autoresTemas', methods=['POST'])
def createUser():
  print(request.json)
  return request.json['name']


@app.route('/', methods=['GET'])
def getUsers():
    return jsonify({"users":"asd"})

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, make_response, g
from graphController import GraphController

import json

# CONFIG
DEBUG = True
app = Flask(__name__)

graph = GraphController()

@app.route('/', defaults={'path': None})
@app.route('/<path:path>')
def index(path):
    return make_response(open('index.html').read())

@app.route('/api/node/<nodeId>', methods = ['GET'])
def getNode(nodeId):
    data = graph.getNodeById(nodeId);
    if not data:
        return json.dumps({'success': False})

    return json.dumps(data)

if __name__ == '__main__':
    app.debug = True
    app.run(port=4000)

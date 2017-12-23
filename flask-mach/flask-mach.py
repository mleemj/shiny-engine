import csv
import json
import os

from flask import Flask, request, Response, stream_with_context
from flask_cors import CORS

from mSettings import MSettings

mach = MSettings()
app = Flask(__name__, instance_path=mach.instance_path)
CORS(app)


@app.route('/upload', methods=['GET', 'POST'])
def uploadData():
    def upload():
        # Access Global request object.
        # In HTML, FormData.append('data', dataFile, dataFile.name);
        dataFile = request.files['data']

        # Read line from file. Line is made of bytes. Decode bytes into String.
        # Strip empty space and split using delimiter comma.
        headers = dataFile.readline().decode().strip().split(',')
        features = []
        for h in headers:
            features.append(h)
        yield json.dumps(features)
        dataFile.save(os.path.join(app.instance_path, dataFile.filename))

    resp = Response(stream_with_context(upload()))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    app.run()

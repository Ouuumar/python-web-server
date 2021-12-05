import unittest
from flask import Flask, jsonify, request
import numpy as np

app = Flask(__name__)


@app.route('/')

def response():
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp

@app.route('/average', methods=['GET'])

def average():
    # http://localhost:5000/home?list=1,2,3    
    data = request.args.get("list") or '0'
    # get rif od the comma in 1,2,3
    data = data.split(',')
    # convert string to numpy array to perform operation int[1,2,3]
    data = np.array(data)
    # convert data to float to perform reduce and math operation float[1,2,3]
    new_data = data.astype(float)

    return str(np.mean(new_data)) # must return a dict or tuple or string in response

if __name__ == '__main__':  
    app.run(debug=True, host='0.0.0.0', port=8080)
    # unittest.main

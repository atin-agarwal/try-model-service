#!flask/bin/python
from flask import Flask,request
import pymongo
import subprocess

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["model_inventory"]


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/v1/tryit', methods=['GET'])
def try_it():
    api_name = request.args.get('apiName')
    print('API Name :: ' + api_name)

    myquery = { "name": api_name }
    myDoc = mycol.find_one(myquery)

    result = myDoc
    print("Result from DB :: ", result)

    modelFileLocation = result['modelFileLocation']
    inputFileLocation = result['inputFileLocation']

    cmd = 'python3 main.py ' + modelFileLocation + ' ' + inputFileLocation
    print('Command running :: ', cmd)

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate() 
    decodedOut = out.decode('utf8')
    print("Err:: ", err)
    print("Output :: " , decodedOut)

    return (decodedOut)
   

if __name__ == '__main__':
    app.run(debug=True)

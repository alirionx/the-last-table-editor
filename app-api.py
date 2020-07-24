#!/usr/bin/python3

#-Import needed modules---------------------------------------------------
import os
import sys
#import shutil
import json
#import datetime
from time import localtime, strftime
from pathlib import Path

#-Global Vars-------------------------------------------------------------
curDir = os.path.abspath(os.getcwd())
scriptDir = os.path.dirname(os.path.realpath(__file__))
curTimestamp = strftime("%Y-%m-%d %H:%M:%S", localtime())
apiDataPath = os.path.join(scriptDir, "api-data")

#-Flask App Definition----------------------------------------------------
from flask import Flask, request, redirect, url_for, send_from_directory, session, render_template, send_file, Response

app = Flask(__name__)
app.secret_key = "changeit"
app.debug = True


#-Helpers Section---------------------------------------------------------
def obj_to_json_http(dataObj):

  resJson = json.dumps(dataObj, indent=2)
  resp = Response(
    response=resJson,
    status=200,
    mimetype="application/json")
  return resp


#-HTML Render Section-----------------------------------------------------

@app.route('/', methods=['GET'])
def root_html():
  return "<h2>the-last-table-editor api</h2>"

#-API Section-------------------------------------------------------------

@app.route('/api/test', methods=['GET'])
def api_test():
  
  dataObj = {
    "request-url": "/api/test",
    "status": "Ok",
    "timestamp": curTimestamp
  }

  resp = obj_to_json_http(dataObj)
  return resp

#-----------------------------------------------

@app.route('/api/config/get', methods=['GET'])
def api_config_get():

  #----------------------------------
  tblDataObj = []
  for dataFileName in sorted(os.listdir(apiDataPath)):
    #print(dataFileName)
    curPath = os.path.join(apiDataPath, dataFileName)
    try:
      fileObj = open(curPath, "r")
      fileStr = fileObj.read()
      fileDataObj = json.loads(fileStr)
    except Exception as err:
      print("Table data file " + curPath + "damaged or not readable") 
      print(str(err))
      continue
    
    if not isinstance(fileDataObj, dict):
      print("File is in wrong format. must be a dictionary") 
      continue

    tblDataObj.append(fileDataObj)

  #----------------------------------

  dataObj = {
    "request-url": "/api/config/get",
    "status": "Ok",
    "timestamp": curTimestamp,
    "data": tblDataObj
  }

  resp = obj_to_json_http(dataObj)
  return resp

#-----------------------------------------------


@app.route('/api/config/set', methods=['POST'])
def api_config_set():

  #----------------------------------
  
  try:
    dataIn = json.loads(request.data)
  except Exception as err:
      msg = "Failed to load json input from post request"
      print(msg) 
      print(str(err))
      return msg, 400
    
  #----------------------------------

  try:
    tblId = int(dataIn["id"])
    flObj = open(os.path.join(apiDataPath, "t"+str(tblId)+".json"), "r")
    print(tblId)
  except Exception as err:
    msg = "invalid ID: " + json.dumps(dataIn, indent=2)
    print(msg) 
    print(str(err))
    return msg, 400

  #----------------------------------

  dataObj = json.loads(flObj.read())
  flObj.close()
  print(dataObj)

  for key, val in dataIn.items():
    dataObj[key] = val

  jsonStr = json.dumps(dataObj, indent=2)
  flObj = open(os.path.join(apiDataPath, "t"+str(tblId)+".json"), "w")
  flObj.write(jsonStr)


  #----------------------------------

  dataObj = {
    "request-url": "/api/config/set",
    "status": "Ok",
    "timestamp": curTimestamp,
    "data": dataIn
  }

  resp = obj_to_json_http(dataObj)
  return resp

#-----------------------------------------------


#-App Runner--------------------------------------------------------------
if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5000)
   
#-------------------------------------------------------------------------

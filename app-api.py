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
  
  tblDataObj = {
    "defi": [
      {
        "col": "id",
        "hl": "Id",
        "align": "center",
        "manda": True
      },
      {
        "col": "name",
        "hl": "Table name",
        "align": "left",
        "manda": True
      },
      {
        "col": "description",
        "hl": "Description",
        "align": "left",
        "manda": False
      }
      ,
      {
        "col": "comment",
        "hl": "Comment",
        "align": "left",
        "manda": False
      }
    ],
    "data": []
  }

  objList = ["definition", "data"]
  missingParas = list

  #----------------------------------
  for dataFileName in sorted(os.listdir(apiDataPath)):
    print(dataFileName)
    curPath = os.path.join(apiDataPath, dataFileName)
    try:
      fileObj = open(curPath, "r")
      fileStr = fileObj.read()
      fileDataObj = json.loads(fileStr)
    except Exception as err:
      print("Table data file " + curPath + "damaged or not readable") 
      print(str(err))
      continue

    missingParas = []

    for col in tblDataObj["defi"]:
      objList.append(col["col"])

    for col in objList:
      if col not in fileDataObj:
        missingParas.append(col)

    if len(missingParas) > 0:
      print("missing parameter [" + ", ".join(missingParas) + "] in Table data file " + curPath)
      continue
    
    rowObj = {}
    for col in tblDataObj["defi"]:
      rowObj[col["col"]] = fileDataObj[col["col"]]

    tblDataObj["data"].append(rowObj)
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


#-App Runner--------------------------------------------------------------
if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5000)
   
#-------------------------------------------------------------------------

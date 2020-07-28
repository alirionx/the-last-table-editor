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

#----------------------------------------------

def get_table_paras_obj():

  tblDataObj = []
  for dataFileName in sorted(os.listdir(apiDataPath)):
    #print(dataFileName)
    if not dataFileName.endswith(".json"):
      continue

    curPath = os.path.join(apiDataPath, dataFileName)
    try:
      fileObj = open(curPath, "r")
      fileStr = fileObj.read()
      fileDataObj = json.loads(fileStr)
    except Exception as err:
      print(str(err))
      print("Table data file " + curPath + "damaged or not readable") 
      continue
    
    if not isinstance(fileDataObj, dict):
      print("File is in wrong format. must be a dictionary") 
      continue

    tblDataObj.append(fileDataObj)

  return tblDataObj

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

#--------------------------------------------------------------

@app.route('/api/config/get', methods=['GET'])
def api_config_get():

  tblDataObj = get_table_paras_obj()

  dataObj = {
    "request-url": "/api/config/get",
    "status": "Ok",
    "timestamp": curTimestamp,
    "data": tblDataObj
  }

  resp = obj_to_json_http(dataObj)
  return resp

#--------------------------------------------------------------

@app.route('/api/tableparas/get/<tblId>', methods=['GET'])
def api_tableparas_get(tblId):

  #----------------------------------
  confPath = os.path.join(apiDataPath, 't' + str(tblId) + '.json')
  try:
    fileObj = open(confPath, "r")
    fileStr = fileObj.read()
    fileDataObj = json.loads(fileStr)
  except Exception as err:
    msg = "Table data file " + confPath + "damaged or not readable"
    print(msg) 
    print(str(err))
    return msg, 404
    
  if not isinstance(fileDataObj, dict):
    msg = "File is in wrong format. must be a dictionary"
    print(msg) 
    return msg, 400


  #----------------------------------

  dataObj = {
    "request-url": "/api/tableparas/get/"+tblId,
    "status": "Ok",
    "timestamp": curTimestamp,
    "data": fileDataObj,
    "id": tblId
  }

  resp = obj_to_json_http(dataObj)
  return resp

#--------------------------------------------------------------

@app.route('/api/tableparas/add', methods=['POST'])
def api_tableparas_add():

  #----------------------------------
  try:
    dataIn = json.loads(request.data)
  except Exception as err:
      msg = "Failed to load json input from post request"
      print(msg) 
      print(str(err))
      return msg, 400
  
  print(dataIn)
  #----------------------------------
  try:
    tblId = dataIn["id"]
  except Exception as err:
    msg = "invalid ID: " + json.dumps(dataIn, indent=2)
    print(str(err))
    return msg, 400

  if tblId != "new":
    msg = "invalid ID: " + str(tblId)
    print(msg)
    return msg, 400

  #----------------------------------

  tblDataObj = get_table_paras_obj()
  idList = []
  for tblParas in tblDataObj:
    idList.append(tblParas["id"])

  newId = False
  i = 0
  while not newId:
    if i not in idList:
      newId = i
    i += 1
  print(newId)
  
  #----------------------------------
  dataObj = {}
  for key, val in dataIn.items():
    dataObj[key] = val

  dataObj["id"] = newId
  dataObj["definition"] = []
  dataObj["data"] = []

  jsonStr = json.dumps(dataObj, indent=2)
  
  #----------------------------------

  newPath = os.path.join(apiDataPath, "t"+str(newId)+".json")
  try:
    flObj = open(newPath, "w")
  except Exception as err:
    msg = "Unable to create config file for new table " + confPath
    print(str(err))
    print(msg) 
    return msg, 400

  flObj.write(jsonStr)
  flObj.close()
  print(dataObj)

  #----------------------------------

  resObj = {
    "request-url": "/api/tableparas/add",
    "status": "Ok",
    "timestamp": curTimestamp,
    "data": dataObj
  }

  resp = obj_to_json_http(resObj)
  return resp


#--------------------------------------------------------------

@app.route('/api/tableparas/edit', methods=['POST'])
def api_tableparas_edit():

  #----------------------------------
  
  try:
    dataIn = json.loads(request.data)
  except Exception as err:
      msg = "Failed to load json input from post request"
      print(str(err))
      print(msg) 
      return msg, 400
    
  #----------------------------------
  try:
    tblId = int(dataIn["id"])
    flPath = os.path.join(apiDataPath, "t"+str(tblId)+".json")
    flObj = open(flPath, "r")
    print(tblId)
  except Exception as err:
    msg = "invalid ID: " + json.dumps(dataIn, indent=2)
    print(str(err))
    print(msg) 
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

#--------------------------------------------------------------
@app.route('/api/tableparas/delete', methods=['POST'])
def api_tableparas_delete():

  #----------------------------------
  
  try:
    dataIn = json.loads(request.data)
  except Exception as err:
      msg = "Failed to load json input from post request"
      print(str(err))
      print(msg) 
      return msg, 400
    
  #----------------------------------
  try:
    tblId = int(dataIn["id"])
    flPath = os.path.join(apiDataPath, "t"+str(tblId)+".json")
  except Exception as err:
    msg = "invalid ID: " + json.dumps(dataIn, indent=2)
    print(str(err))
    print(msg) 
    return msg, 400

  if not os.path.isfile(flPath):
    msg = "invalid ID (file does not exist): " + flPath
    print(str(err))
    print(msg) 
    return msg, 400

  #----------------------------------

  try:
    os.remove(flPath)
  except Exception as err:
    msg = "Failed to delete file: " + flPath
    print(str(err))
    print(msg) 
    return msg, 400

  #----------------------------------

  dataObj = {
    "request-url": "/api/tableparas/delete",
    "status": "Ok",
    "timestamp": curTimestamp,
    "data": dataIn,
    "file": flPath
  }

  resp = obj_to_json_http(dataObj)
  return resp

#--------------------------------------------------------------

@app.route('/api/tableconfig/apply/<tblId>', methods=['POST'])
def api_tableconfig_apply(tblId):

  #----------------------------------
  confPath = os.path.join(apiDataPath, 't' + str(tblId) + '.json')
  try:
    fileObj = open(confPath, "r")
    fileStr = fileObj.read()
    fileDataObj = json.loads(fileStr)
    fileObj.close()
  except Exception as err:
    msg = "Table data file " + confPath + "damaged or not readable"
    print(msg) 
    print(str(err))
    return msg, 404
    
  if not isinstance(fileDataObj, dict):
    msg = "File is in wrong format. must be a dictionary"
    print(msg) 
    return msg, 400

  #----------------------------------
  try:
    dataIn = json.loads(request.data)
  except Exception as err:
      msg = "Failed to load json input from post request"
      print(str(err))
      print(msg) 
      return msg, 400
    
  #----------------------------------
  try:
    fileDataObj["definition"] = dataIn
    jsonStr = json.dumps(fileDataObj, indent=2)
    fileObj = open(confPath, "w")
    fileObj.write(jsonStr)
    fileObj.close()
  except:
    msg = "Failed to write defi data to file"
    print(str(err))
    print(msg) 
    return msg, 400
    
  #----------------------------------

  dataObj = {
    "request-url": "/api/tableconfig/apply/"+tblId,
    "status": "Ok",
    "timestamp": curTimestamp,
    "data": fileDataObj,
    "id": tblId
  }

  resp = obj_to_json_http(dataObj)
  return resp

#--------------------------------------------------------------


#-App Runner--------------------------------------------------------------
if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5000)
   
#-------------------------------------------------------------------------

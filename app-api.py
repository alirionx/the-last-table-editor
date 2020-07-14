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


#-App Runner--------------------------------------------------------------
if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5000)
   
#-------------------------------------------------------------------------

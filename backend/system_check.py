
import sys
import os
import importlib

class globalvars:
  PYVER = 3
  MODLIST = ["json", "flask"] 
  FAIL = '\033[91m'
  ENDC = '\033[0m'


def system_check():
  pyVer = int(sys.version_info.major)
  if pyVer != globalvars.PYVER:
    msg = 'Unssuported python version! Please use python V'+str(globalvars.PYVER)
    print(f'{globalvars.FAIL}'+msg+f'{globalvars.ENDC}')
    exit()

  toInst = []
  for mod in globalvars.MODLIST:
    try:
      chk = importlib.import_module(mod)
    except:
      toInst.append(mod)

  if len(toInst) > 0:
    msg = 'Module import failed: Please install the following python modules: '+', '.join(toInst)
    print(f'{globalvars.FAIL}'+msg+f'{globalvars.ENDC}')
    exit()
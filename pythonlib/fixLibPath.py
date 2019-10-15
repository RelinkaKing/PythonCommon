import os
import sys
import shutil
import site


print(site.getsitepackages())
print(os.getcwd())
pthFileName = "MyPyhonLib.pth"
with open(pthFileName,'w') as f:
    f.writelines(os.getcwd().replace("\\","/"))

for path in site.getsitepackages():
    if os.path.isdir(path) and "site-packages" in path:
        tmpFile = os.path.join(path,pthFileName)
        if os.path.isfile(tmpFile):
            os.remove(tmpFile)
        shutil.copyfile(pthFileName,tmpFile)

#from MyPythonLib.Util import *
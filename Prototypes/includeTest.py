#! /env/bin/python

import os, sys, pdb
from types import ClassType

try:
    sys.path.insert(0, './Types')
    classes = []
    for f in os.listdir("Types"):
        if f.endswith(".py"):
            
            fileName = f[0:f.rfind('.')]
            exec("import " + fileName)
            exec("moduleObj = " + fileName)

            #exec("classes = [x for x in dir(fileName) if isinstance(getattr(" + fileName + ", x))]")
            localClasses = [x for x in dir(moduleObj) if isinstance(getattr(moduleObj, x), ClassType)]
            
            for c in localClasses:
                classes.append(fileName + "." + c)

    print classes
    exec("a = " + classes[0] + "()")
    print a

except OSError:
    print "No directory 'Types' found"

#p = ast.parse(source)
#classes = [node.name for node in ast.walk(p) if isinstance(node, ast.ClassDef)]

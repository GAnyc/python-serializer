#!/usr/bin/python

import os, sys, pdb
from types import ClassType
from pprint import pprint

def run():
    global includeTypes

    classTypes = []

    #### 
    # first load all the class names
    try:
        sys.path.insert(0, './Types')
       
        for fname, cname in includeTypes:
            if cname not in classTypes:
                exec( "from " + fname + " import " + cname )
                exec( "classObj = " + cname )
                classTypes.append(classObj)
            else:
                print "Importing dupe class: ", cname

        print classTypes

    except OSError:
        print "No directory 'Types' found"
        return
    

    #### 
    #  Then instantiate the classes
    #  This is where we ignore dupes
    classInstances = []
    
    for t in classTypes:
        found = False
        for i in classInstances:
            if isinstance(i, t):
                found = True
                break

        if not found:
            print "Runner instantiating type ", t
            classInstances.append(t(classTypes, classInstances))
            
    print len(classInstances), " - RESULTS:"
    for t in classInstances:
        pprint(t.JSON())
        print "---"




                #   ["fileName", "className"],    
includeTypes =  [   [ "relationTest", "RelationTest" ],
                    [ "testClass", "TestClass"] 
                ]

if __name__ == "__main__":
    run()

#!/usr/bin/env python

'''
mattplotlib/el-skel/jared_esqueleto.py
Make an empty EventLoop algorithm skeleton.

This is meant to replace the old
$ROOTCOREBIN/user_scripts/EventLoop/make_skeleton MyAnalysis MyxAODAnalysis
(for lazy people)

Templates are taken from
https://atlassoftwaredocs.web.cern.ch/ABtutorial/create_algorithm/

Matt LeBlanc <matt.leblanc@cern.ch> 2017/07/24
'''

import os
import logging
import inspect
from optparse import OptionParser

logging.basicConfig(level=logging.INFO)

parser = OptionParser()

cdir = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
print cdir

###
# options
# job configuration
parser.add_option("--package", help="Which package to add your algo to?", default="MyAnalysis")
parser.add_option("--algo", help="What is your algorithm going to be named?", default="MyxAODAnalysis")

(options, args) = parser.parse_args()

# do stuff
if(not os.path.exists(cdir+'/'+options.package+'/Root/'+options.algo+'.cxx')):

    f1 = open(cdir+'/MyxAODAnalysis.cxx', 'r')
    f2 = open(options.package+'/Root/'+options.algo+'.cxx', 'w')
    for line in f1:
        line = line.replace('MyAnalysis', options.package)
        line = line.replace('MyxAODAnalysis', options.algo)
        f2.write(line)
    f1.close()
    f2.close()

    f1 = open(cdir+'/MyxAODAnalysis.h', 'r')
    f2 = open(options.package+'/'+options.package+'/'+options.algo+'.h', 'w')
    for line in f1:
        line = line.replace('MyAnalysis', options.package)
        line = line.replace('MyxAODAnalysis', options.algo)
        f2.write(line)
    f1.close()
    f2.close()

    f1 = open(cdir+'/MyAnalysisDict.h', 'r')
    f2 = open(options.package+'/'+options.package+'/'+options.package+'Dict.h', 'w')
    for line in f1:
        line = line.replace('MyAnalysis', options.package)
        line = line.replace('MyxAODAnalysis', options.algo)
    f2.write(line)
    f1.close()
    f2.close()

    f1 = open(cdir+'/selection.xml', 'r')
    f2 = open(options.package+'/'+options.package+'/selection.xml', 'w')
    for line in f1:
        line = line.replace('MyAnalysis', options.package)
        line = line.replace('MyxAODAnalysis', options.algo)
    f2.write(line)
    f1.close()
    f2.close()

    f1 = open(cdir+'/CMakeLists.txt', 'r')
    f2 = open(options.package+'/'+options.package+'/CMakeLists.xml', 'w')
    for line in f1:
        line = line.replace('MyAnalysis', options.package)
        line = line.replace('MyxAODAnalysis', options.algo)
    f2.write(line)
    f1.close()
    f2.close()

    if(not os.path.exists(options.package+'/Root/LinkDef.h')):
        f1 = open(cdir+'/LinkDef.h', 'r')
        f2 = open(options.package+'/Root/LinkDef.h', 'w')
        for line in f1:
            line = line.replace('MyAnalysis', options.package)
            line = line.replace('MyxAODAnalysis', options.algo)
            f2.write(line)
        f1.close()
        f2.close()
    else:
        # just insert the line
        logging.info("LinkDef.h exists\tAppending new info.")
        f = open(options.package+'/Root/LinkDef.h', "r")
        contents = f.readlines()
        f.close()
        contents.insert(12, '\n#pragma link C++ class '+options.algo+'+;\n')
        f = open(options.package+'/Root/LinkDef.h', "w")
        contents = "".join(contents)
        f.write(contents)
        f.close()
        
    if(not os.path.exists(options.package+'/CMakeLists.txt')):
        f1 = open(cdir+'/CMakeLists.txt', 'r')
        f2 = open(options.package+'/CMakeLists.txt', 'w')
        for line in f1:
            line = line.replace('MyAnalysis', options.package)
            line = line.replace('MyxAODAnalysis', options.algo)
            f2.write(line)
        f1.close()
        f2.close()
    else:
        logging.info("CMakeLists.txt exists\tTaking no action.")

    logging.info("Done.")
    os.system('ls -lhr '+options.package)

else:
    logging.info("This algorithm exists! Aborting.")

# -*- coding: utf-8 -*-
'''
Created on 20.12.2014

@author: Simon Gwerder
'''

import timeit

from maintenance import Maintenance
from taginfo.taginfo import TagInfo
from thesaurus.rdfgraph import RDFGraph
from thesaurus.updatethesaurus import UpdateThesaurus
from utilities import utils
from utilities.configloader import ConfigLoader

if __name__ == '__main__':
    '''Start script to update automatically'''
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')
    startTime = timeit.default_timer()
    retry = True
    console = Maintenance(sys.stdout)
    cl = ConfigLoader()
    outputName = cl.getThesaurusString('OUTPUT_NAME')
    outputEnding = cl.getThesaurusString('DEFAULT_FORMAT')
    rdfGraph = RDFGraph(utils.outputFile(utils.dataDir(), outputName, outputEnding, useDateEnding=False))
    tagInfo = TagInfo()
    UpdateThesaurus(tagInfo, rdfGraph, console)

    endTime = timeit.default_timer()
    elapsed = endTime - startTime
    console.println('\nTime elapsed to update rdfGraph: ' + str(elapsed / 60) + ' mins')
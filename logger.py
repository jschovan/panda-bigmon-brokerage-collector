# -*- coding: utf-8 -*-

def logger(name="PandaBrokerageMonitor", file="/tmp/logger.log"):
    import logging
    loggerO = logging.getLogger(name)
    
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    
    hdlr = logging.FileHandler(file)
    hdlr.setFormatter(formatter)
    
    loggerO.addHandler(hdlr) 
    #loggerO.setLevel(logging.DEBUG)
    loggerO.setLevel(logging.INFO)
    
    return loggerO

"""
logger.error('We have a problem')
logger.info('While this is just chatty')
"""



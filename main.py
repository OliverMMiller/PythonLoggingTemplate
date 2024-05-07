#Wiki:
#https://docs.python.org/3/howto/logging.html
#Logging Cookbook:
#https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook

import logging
levels= [logging.NOTSET, logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]
levelnumss = [0, 10, 20, 30, 40, 50]
logging.setLevel(levels[3])

#also can work with threading module 
#import threading

#logging to a file?
#logger = logging.getLogger(__name__)
#logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

print()
logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical() 
import logging
import os
import time


#timestamp = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
#filePath = os.path.dirname(__file__)
filePath = os.getcwd()
logFile = os.path.join(filePath, "factoryBench.log")
handler = logging.FileHandler(logFile)
formatter = logging.Formatter('[%(asctime)s][%(levelname)s]\n%(message)s')
handler.setFormatter(formatter)
handler2 = logging.StreamHandler()
handler2.setFormatter(formatter)


logger = logging.getLogger()
logger.addHandler(handler)
logger.addHandler(handler2)
logger.setLevel(logging.NOTSET)


LOGGER_ERROR = logger.error
LOGGER_DEBUG = logger.debug
LOGGER_INFO  = logger.info

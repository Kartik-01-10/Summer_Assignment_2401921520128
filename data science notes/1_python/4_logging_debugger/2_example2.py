import logging
logging.basicConfig(filename="test2.log" , level= logging.DEBUG ,format='%(asctime)s %(name)s %(levelname)s %(message)s')

# Logging messages
logging.info("this is my info logging")
logging.error("this is my error msg")
logging.critical("this is my critical")
logging.shutdown()
# o/p of this code is test2.text file 

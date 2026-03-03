import logging


logging.basicConfig(
    filename="test1.log",
    level=logging.DEBUG,
    format='%(asctime)s %(message)s'
)

# Logging messages
logging.info("this is my info logging")
logging.error("this is my error msg")
logging.critical("this is my critical")
logging.shutdown()


#### the file named test1 is the output of this program

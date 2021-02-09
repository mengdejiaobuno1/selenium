import logging
import os

logging.basicConfig(level=logging.INFO, filename=os.path.join(os.getcwd(), 'log.log'))
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
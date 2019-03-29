import logging

logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger(__name__)

# create a file handler
handler = logging.FileHandler('cart_Log.log')

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
LOG.addHandler(handler)

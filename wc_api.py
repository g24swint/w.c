
# coding: utf-8

# In[14]:

import sqlite3 as db
import sqlalchemy as sa
import logging as logging
import sys


# In[ ]:

# "global" variables
wc_log = None


# In[53]:

def _init_logs(reset_handlers=True):
    """Create a sys.stdout logger for w_c and print startup information 
    
    The logger name is the "w_c" namespace
    """
    global wc_log
    log = logging.getLogger("w_c")
    if reset_handlers:
        log.handlers = []
        log_stream = logging.StreamHandler(sys.stdout)
        log_formatter = logging.Formatter('%(asctime)s::%(name)s::%(levelname)s::%(message)s')
        log_stream.setFormatter(log_formatter)
        log.addHandler(log_stream)
        log.setLevel(logging.DEBUG)
    log.debug("Versions:")
    log.debug("  slqalchemy: {}".format(sa.__version__))
    log.debug("     sqlite3: {}".format(db.version))
    wc_log = log

_init_logs()


# In[50]:




# In[7]:

get_ipython().magic('pinfo logging.StreamHandler')


# In[ ]:




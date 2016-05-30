
# coding: utf-8

# In[9]:

import sqlite3 as db
import sqlalchemy as sa
import logging as logging
import sys


# In[10]:

#fhandler = log.FileHandler(filename='mylog.log', mode='a')
log = logging.getLogger("w_c")
log_stream = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_stream.setFormatter(formatter)
log.addHandler(log_stream)
log.setLevel(logging.DEBUG)


# In[12]:

log.debug("Versions:")
log.debug("  slqalchemy: {}".format(sa.__version__))
log.debug("     sqlite3: {}".format(db.version))


# In[ ]:

sa.__version__


# In[7]:

get_ipython().magic('pinfo logging.StreamHandler')


# In[ ]:




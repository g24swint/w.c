
# coding: utf-8

# In[1]:

'''w.c The wild.chicken top level module for managing tasks'''

import sys
import os
import datetime as dt
import time
import logging


from ._setup_routines import _init_logs, _get_db_name
from w_c.wc_api import *


# turn on logging by default
_init_logs(reset_handlers=False)
print("Logger from init is %s" % logging.getLogger("w_c"))


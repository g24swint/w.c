
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


# In[5]:

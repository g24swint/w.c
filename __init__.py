
# coding: utf-8

# In[1]:

'''w.c The wild.chicken top level module for managing tasks'''

import sys
import os
import datetime as dt
import time
import logging


from _setup_routines import _init_logs, _setup_engine


# In[2]:

print(__name__)
if __name__ == '__main__':
    print('Running main')
    wc_log = _init_logs()
    db_engine = _setup_engine()    


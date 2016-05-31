
# coding: utf-8

# In[1]:

'''w.c The wild.chicken top level module for managing tasks'''

import sys
import os
import datetime as dt
import time
import logging


from _setup_routines import _init_logs, _setup_engine


# In[ ]:

def standalone_exec():
    print('Running main')
    wc_log = _init_logs()
    db_engine = _setup_engine() 
    session = _open_session(db_engine)
    add_task(session, desc="Buy weekly groceries", orig_comp=dt.datetime(2016, 5, 29), for_whom=1)
    return 0


# In[2]:

print(__name__)

if __name__ == '__main__':
    standalone_exec()


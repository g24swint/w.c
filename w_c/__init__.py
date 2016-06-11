
# coding: utf-8

# In[1]:

'''w.c The wild.chicken top level module for managing tasks'''

import sys
import os
import datetime as dt
import time
import logging


from ._setup_routines import _init_logs, _get_db_name
import w_c.wc_api as wc


# In[5]:

def standalone_exec():
    print('Running main')
    wc_log = _init_logs()
    wc_tasks = TaskEngine(_get_db_name())
    wc_tasks.add_task(session, desc="Buy weekly groceries", orig_comp=dt.datetime(2016, 5, 29), for_whom=1)
    wc_tasks.list_tasks(session)
    return 0


# In[6]:

print(__name__)

if __name__ == '__main__':
    standalone_exec()


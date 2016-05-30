
# coding: utf-8

# In[1]:

import sys
import os

import sqlite3 as db
import sqlalchemy as sa
import logging as logging

import datetime as dt
import time

from _setup_routines import _init_logs, _setup_engine


# In[2]:

# "global" variables
wc_log = None
db_engine = None


# In[3]:

wc_log = _init_logs()


# In[4]:

db_engine = _setup_engine()


# In[ ]:




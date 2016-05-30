
# coding: utf-8

# In[1]:

import sys
import os

import sqlite3 as db
import sqlalchemy as sa
import logging as logging

import datetime as dt
import time


# In[2]:

# "global" variables
wc_log = None
startup_path = os.getcwd()
db_dir = None
db_engine = None


# In[3]:

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
    log.debug("Starting in %s" % startup_path)
    log.debug("Versions:")
    log.debug("  slqalchemy: {}".format(sa.__version__))
    log.debug("     sqlite3: {}".format(db.version))
    wc_log = log

_init_logs()


# In[5]:

def _setup_engine():
    '''Set the '''
    global db_dir, db_engine 
    db_dir = os.path.join(os.path.dirname(startup_path),'db')
    db_name = os.path.join(db_dir, "work_cards.db")
    wc_log.debug(" db_dir:: %s" % db_dir)
    wc_log.debug("db_name:: %s" % db_name)
    db_engine = sa.create_engine("sqlite:///" + db_name )
    
_setup_engine()


# In[6]:

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


# In[7]:


class Tasks(Base):
    '''SQLAlchemy Tasks class that maps all tasks to the tasks table
    
    Task descriptions default to Twitter length strings :-)
    '''
    __tablename__ = "tasks"
    id = sa.Column(sa.Integer, primary_key = True)
    desc = sa.Column(sa.String(140))
    orig_comp = sa.Column(sa.DateTime)
    cur_comp = sa.Column(sa.DateTime)
    for_whom = sa.Column(sa.Integer)
    
    def __repr__(self):
        return "Task {id}: ({desc}, {orig_comp}, {cur_comp}, {for_whom})".format(
        self )
    


# In[8]:

Tasks.__table__


# In[11]:

Base.metadata.create_all(db_engine)


# In[10]:




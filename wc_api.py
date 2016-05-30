
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


# In[4]:

def _setup_engine():
    '''Set the database executioin file and create a db directory if none exists'''
    global db_dir, db_engine 
    db_dir = os.path.join(os.path.dirname(startup_path),'db')
    if not os.path.exists(db_dir):
        os.mkdir(db_dir)
    db_name = os.path.join(db_dir, "work_cards.db")
    wc_log.debug(" db_dir:: %s" % db_dir)
    wc_log.debug("db_name:: %s" % db_name)
    db_engine = sa.create_engine("sqlite:///" + db_name )
    
_setup_engine()


# In[5]:

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


# In[6]:


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
    status = sa.Column(sa.String(140))
    
    def __repr__(self):
        return "Task {}: ({}, {}, {}, {}, {})".format(
        self.id, self.desc, self.orig_comp, self.cur_comp, self.for_whom,
        self.status)
    


# In[7]:

Tasks.__table__


# In[8]:

Base.metadata.create_all(db_engine)


# In[9]:

first_task = Tasks(desc = "Buy weekly groceries", orig_comp=dt.datetime(2016, 5, 29),
                  cur_comp=dt.datetime(2016, 6, 4), for_whom=1, status="Todo")


# In[10]:

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=db_engine)


# In[11]:

session = Session()


# In[12]:

session.add(first_task)


# In[13]:

session.commit()


# In[15]:

def add_task(desc, orig_comp, for_whom):
    '''Adds a task to the tasks list.
    
    Params:
        desc: description of the task
        orig_comp: the original completion date set for the task
        cur_comp: the current completion date on the task
        for_whom: task for whom its being completed
        
    Returns:
        nada
    '''
    task_to_add = Tasks(desc=desc, orig_comp=orig_comp, cur_comp=orig_comp, 
                        status="Todo", for_whom=for_whom)
    session.add(task_to_add)
    session.commit()

add_task(desc="Buy weekly groceries", orig_comp=dt.datetime(2016, 5, 29), for_whom=1)


# In[16]:

for task in session.query(Tasks).filter_by():
    print(task)



# coding: utf-8

# In[1]:

import sqlite3 as db
import sqlalchemy as sa
import logging as logging

import datetime as dt
import time


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
        return "Task {.id}: ({.desc}, {.orig_comp}, {.cur_comp}, {.for_whom}, {.status})".format(
        self)
    


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
        id for the added task
    '''
    log = logging.getLogger(__name__)
    task_to_add = Tasks(desc=desc, orig_comp=orig_comp, cur_comp=orig_comp, 
                        status="Todo", for_whom=for_whom)
    session.add(task_to_add)
    session.commit()
    log.debug("added task: {}".format(str(task_to_add)))
    return task_to_add.id

add_task(desc="Buy weekly groceries", orig_comp=dt.datetime(2016, 5, 29), for_whom=1)


# In[1]:

for task in session.query(Tasks).filter_by():
    print(task)


# In[ ]:

def update_task(id, desc,)


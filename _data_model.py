
# coding: utf-8

# In[ ]:

import sqlite3 as db
import sqlalchemy as sa
import logging as logging

import datetime as dt
import time


# In[ ]:

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


# In[ ]:

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
    



# coding: utf-8

# In[1]:

'''_data_model.py contains the data models for the essential parts of the 
todo lists in several major classes.
'''
import sqlalchemy as sa


# In[2]:

# disable pylint squawks when using Declarative
# pylint: disable=too-few-public-methods,invalid-name

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


# In[3]:

class Task(Base):
    '''SQLAlchemy Tasks class that maps all tasks to the tasks table
    
    Task descriptions default to Twitter length strings :-)
    '''
    __tablename__ = "tasks"
    tid = sa.Column(sa.Integer, primary_key=True)
    desc = sa.Column(sa.String(140))
    orig_comp = sa.Column(sa.DateTime)
    cur_comp = sa.Column(sa.DateTime)
    for_whom = sa.Column(sa.String(140))
    status = sa.Column(sa.String(140))
    
    def __repr__(self):
        #pylint: disable=line-too-long
        return ("Task {0.tid}: ({0.desc}, {0.orig_comp}, {0.cur_comp}, " +                 "{0.for_whom}, {0.status})").format(self)


# In[4]:

def test_Task_print():
    import datetime as dt
    first_task = Task(desc="Buy weekly groceries", orig_comp=dt.datetime(2016, 5, 29),
                      cur_comp=dt.datetime(2016, 6, 4), for_whom="Galen", status="Todo")
    print(first_task)
test_Task_print()


# In[5]:

import datetime as dt
first_task = Task(desc="Buy weekly groceries", orig_comp=dt.datetime(2016, 5, 29),
                   cur_comp=dt.datetime(2016, 6, 4), for_whom=1, status="Todo")


# In[6]:

("Task {0.tid}: ({0.desc}, {0.orig_comp}, {0.cur_comp}, "+"{0.for_whom}, {0.status})").format(first_task)


# In[ ]:




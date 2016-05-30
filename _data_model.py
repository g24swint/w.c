
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


class Tasks(Base):
    '''SQLAlchemy Tasks class that maps all tasks to the tasks table
    
    Task descriptions default to Twitter length strings :-)
    '''
    __tablename__ = "tasks"
    tid = sa.Column(sa.Integer, primary_key=True)
    desc = sa.Column(sa.String(140))
    orig_comp = sa.Column(sa.DateTime)
    cur_comp = sa.Column(sa.DateTime)
    for_whom = sa.Column(sa.Integer)
    status = sa.Column(sa.String(140))
    
    def __repr__(self):
        #pylint: disable: line-too-long
        return "Task {.tid}: ({.desc}, {.orig_comp}, {.cur_comp}, " +                 "{.for_whom}, {.status})".format(self)


# In[ ]:




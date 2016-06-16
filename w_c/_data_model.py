'''_data_model.py contains the data models for the essential parts of the
todo lists in several major classes.
'''
import sqlalchemy as sa



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




# coding: utf-8

# In[1]:

'''w.c task management API including

add_task
update_task

'''
import logging as logging
import datetime as dt

import sqlalchemy as sa


# In[2]:

from _data_model import *


# In[14]:

def list_tasks(session):
    '''Return a list of all tasks.
    
    Params:
        session: an open session object
    Returns:
        list of all tasks in the db
    '''
    log = logging.getLogger(__name__)
    all_tasks = session.query(Tasks).all()
    log.debug("All tasks", (all_tasks))
    print(all_tasks)
    return all_tasks


# In[4]:

def add_task(session, desc, orig_comp, for_whom):
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
    log.debug("added task: %s", (str(task_to_add)))
    return task_to_add.tid



# In[5]:

def update_task():
    pass


# In[15]:

if __name__=="__main__":
    from _setup_routines import _init_logs, _setup_engine, _open_session
    _init_logs()
    
    db_engine = _setup_engine()
    
    # drop all in the db and rebuild
    Base.metadata.drop_all(db_engine)
    Base.metadata.create_all(db_engine)
    
    first_task = Tasks(desc="Buy weekly groceries", orig_comp=dt.datetime(2016, 5, 29),
                      cur_comp=dt.datetime(2016, 6, 4), for_whom=1, status="Todo")

    session = _open_session(db_engine)

    session.add(first_task)

    session.commit()

    list_tasks(session)


# In[ ]:




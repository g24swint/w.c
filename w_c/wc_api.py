
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


# In[19]:

class TaskList():
    def __init__(self, db_name):
        self.log = logging.getLogger(__name__)
        self.db_name = db_name
        self.db_engine = self._create_engine(db_name)
        self.session = self._open_session()
    
    def _create_engine(self, db_name):
        '''Set the database execution file and create a db directory if none exists

        Params:
            db_dir: directory where the sqlite3 db shall be put

        Returns:
            sqlalchemy engine object
        '''
        db_engine = sa.create_engine("sqlite:///" + db_name)
        return db_engine   
    
    def _open_session(self):
        '''Set an open session object to our backing data store

        Params:
            db_engine: a valid sqlalchemy database engine

        Returns:
            an open Session object referenced by this object
        '''
        from sqlalchemy.orm import sessionmaker
        #pylint: disable=invalid-name
        Session = sessionmaker(bind=self.db_engine)
        #pylint: enable=invalid-name
        self.session = Session()
        return self.session
    
    def list(self, session):
        '''Return a list of all tasks.

        Params:
            session: an open session object
        Returns:
            list of all tasks in the db
        '''
        all_tasks = session.query(Tasks).all()
        self.log.debug("All tasks", (all_tasks))
        print(all_tasks)
        return all_tasks
    
    def add(self, session, desc, orig_comp, for_whom):
        '''Adds a task to the tasks list.

        Params:
            desc: description of the task
            orig_comp: the original completion date set for the task
            cur_comp: the current completion date on the task
            for_whom: task for whom its being completed

        Returns:
            id for the added task
        '''
        task_to_add = Tasks(desc=desc, orig_comp=orig_comp, cur_comp=orig_comp, 
                            status="Todo", for_whom=for_whom)
        session.add(task_to_add)
        session.commit()
        self.log.debug("added task: %s", (str(task_to_add)))
        return task_to_add.tid
    def update_task(self):
        pass
    


# In[20]:

if __name__=="__main__":
    from _setup_routines import _init_logs, _get_db_name
    _init_logs()
    
    db_dir = _get_db_name()
    
    task_list = TaskList(db_dir)
    # drop all in the db and rebuild
    Base.metadata.drop_all(task_list.db_engine)
    Base.metadata.create_all(task_list.db_engine)
    

    first_task = Tasks(desc="Buy weekly groceries", orig_comp=dt.datetime(2016, 5, 29),
                      cur_comp=dt.datetime(2016, 6, 4), for_whom=1, status="Todo")

    
    task_list.add(first_task)

    task_list.list(session)


# In[ ]:




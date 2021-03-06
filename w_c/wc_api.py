
# coding: utf-8

# In[1]:

'''w.c task management API including

add_task
update_task

'''
import logging as logging
import datetime as dt

import sqlalchemy as sa


from ._data_model import *

class TaskList():
    def __init__(self, db_name):
        self.log = logging.getLogger("w_c")
        self.log.critical("db_name is : %s" % db_name)
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
        self.log.debug("db_name: %s" % db_name)
        db_engine = sa.create_engine("sqlite:///" + str(db_name))
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

    def init(self):
        '''Clean all tasks out of the list.

        Params:
            session: an open sql alchemy session attached the to the tasks db

        Returns:
            none
        '''
        # drop all in the db and rebuild
        self.log.critical("Dropping and creating the task db")
        Base.metadata.drop_all(self.db_engine)
        Base.metadata.create_all(self.db_engine)

    def list(self):
        '''Return a list of all tasks.

        Params:
            session: an open session object
        Returns:
            list of all tasks in the db
        '''
        all_tasks = self.session.query(Task).all()
        self.log.debug("All tasks %s", all_tasks)
        #print(all_tasks)
        return all_tasks

    def add(self, desc, orig_comp, for_whom):
        '''Adds a task to the tasks list.

        Params:
            desc: description of the task
            orig_comp: the original completion date set for the task
            cur_comp: the current completion date on the task
            for_whom: task for whom its being completed

        Returns:
            id for the added task
        '''
        task_to_add = Task(desc=desc, orig_comp=orig_comp, cur_comp=orig_comp,
                            status="Todo", for_whom=for_whom)
        self.session.add(task_to_add)
        self.session.commit()
        self.log.debug("added task: %s", (str(task_to_add)))
        return task_to_add.tid

    def update_task(self):
        pass




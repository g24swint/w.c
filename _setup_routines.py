
# coding: utf-8

# In[ ]:

"""_setup_routines submodule initializes logger and data base locations.

Will likely be replaced by more robust config-file style of startup"""
import sys
import os

import logging

import sqlite3 as db
import sqlalchemy as sa


# In[ ]:

STARTUP_PATH = os.getcwd()


# In[ ]:

def _init_logs(reset_handlers=True):
    """Create a sys.stdout logger for w_c and print startup information 
    
    The logger name is the "w_c" namespace
    
    Params:
        reset_handlers: will clear all handlers if True
    
    Returns:
        The Logger object
    """
    log = logging.getLogger(__name__)
    if reset_handlers:
        log.handlers = []
        log_stream = logging.StreamHandler(sys.stdout)
        log_formatter = logging.Formatter('%(asctime)s::%(name)s::%(filename)'+
                                          's::%(levelname)s::%(message)s')
        log_stream.setFormatter(log_formatter)
        log.addHandler(log_stream)
        log.setLevel(logging.DEBUG)
    log.debug("Starting in %s" % STARTUP_PATH)
    log.debug("Versions:")
    log.debug("  slqalchemy: %s" % sa.__version__)
    log.debug("     sqlite3: %s" % db.version)
    return log

def _setup_engine(db_dir=None):
    '''Set the database executioin file and create a db directory if none exists
    
    Params:
        db_dir: directory where the sqlite3 db shall be put
        
    Returns:
        sqlalchemy engine object
    '''
    log = logging.getLogger(__name__)
    db_dir = os.path.join(os.path.dirname(STARTUP_PATH), 'db')
    if not os.path.exists(db_dir):
        os.mkdir(db_dir)
    db_name = os.path.join(db_dir, "work_cards.db")
    log.debug(" db_dir:: %s" % db_dir)
    log.debug("db_name:: %s" % db_name)
    db_engine = sa.create_engine("sqlite:///" + db_name)
    return db_engine


# coding: utf-8
"""_setup_routines submodule initializes logger and data base locations.

Will likely be replaced by more robust config-file style of startup"""
import sys
import os

import logging

import sqlite3 as db
import sqlalchemy as sa
STARTUP_PATH = os.getcwd()


# In[3]:

def _init_logs(reset_handlers=True):
    """Create a sys.stdout logger for w_c and print startup information 
    
    The logger name is the "w_c" namespace
    
    Params:
        reset_handlers: will clear all handlers if True
    
    Returns:
        The Logger object
    """
    log = logging.getLogger("w_c")
    if reset_handlers:
        print("LOGGER IS ", log)

        log.handlers = []
        log_stream = logging.StreamHandler(sys.stdout)
        log_formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)'+
                                          's:%(funcName)s:%(message)s')
        log_stream.setFormatter(log_formatter)
        log.addHandler(log_stream)
        log.setLevel(logging.DEBUG)
    log.debug("Starting in %s", (STARTUP_PATH))
    log.debug("Versions:")
    log.debug("  slqalchemy: %s", (sa.__version__))
    log.debug("     sqlite3: %s", (db.version))
    return log

def _get_db_name():
    '''Calculate our db_dir if needed and relative to our cwd
    Returns:
        Absolute path to our db directory'''
    log = logging.getLogger(__name__)
    db_dir = os.path.join(os.path.dirname(STARTUP_PATH), 'db')
    if not os.path.exists(db_dir):
        os.mkdir(db_dir)
    db_name = os.path.join(db_dir, "work_cards.db")
    log.debug(" db_dir:: %s", (db_dir))
    log.debug("db_name:: %s", (db_name))
    return db_name




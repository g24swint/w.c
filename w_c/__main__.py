

print("W.C version 201606")


import logging
import click
from ._setup_routines import _init_logs

@click.group()
def workcard():
    pass


@workcard.command()
def clean(**kwargs):
    print("clean card:", kwargs)

@workcard.command()
def add(**kwargs):
    print("add task: ", kwargs)

@workcard.command()
def add_goal(**kwargs):
    print("add goal: ", kwargs)

@workcard.command()
def list_tasks(**kwargs):
    pass



if __name__ == "__main__":
    wc_log = _init_logs()
    wc_log.info("Running __main__")
    wc_tasks = TaskEngine(_get_db_name())
    workcard()
    wc_tasks.add_task(session, desc="Buy weekly groceries", orig_comp=dt.datetime(2016, 5, 29), for_whom=1)
    wc_tasks.list_tasks(session)


# In[6]:



if __name__ == '__main__':
    standalone_exec()

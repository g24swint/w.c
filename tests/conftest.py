import pytest
import logging


@pytest.fixture(scope='session')
def db_test_dir(tmpdir_factory):
    fn = tmpdir_factory.mktemp('data').join('test_task_list')
    return fn

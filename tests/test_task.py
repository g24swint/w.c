import sys
import logging
import pytest

import w_c

@pytest.fixture(scope='session')
def test_logger():
    w_c._init_logs(reset_handlers=True)
    test_logger = logging.getLogger("w_c")
    test_logger.setLevel(logging.DEBUG)
    return test_logger


class TestTask:
    def test_init(self, db_test_dir, test_logger):
        test_logger.info("RUNNING TEST ONE")
        tl = w_c.TaskList(db_test_dir)
        tl.init()
        full_list = tl.list()
        assert full_list == []

    def test_add(selfself, db_test_dir, test_logger):
        import datetime
        test_logger.info("RUNNING TEST ONE")
        tl = w_c.TaskList(db_test_dir)
        tl.add("Testing tastk1", for_whom='Galen', orig_comp = datetime.datetime.now())
        full_list = tl.list()
        assert len(full_list) == 1


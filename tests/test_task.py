import pytest

import w_c

class TestTask:
    def test_one(self):
        a = 1
        assert a==1
    def test_two_fail(self):
        b = 1
        assert b==5

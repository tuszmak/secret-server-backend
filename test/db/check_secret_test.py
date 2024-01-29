from datetime import datetime
import pytest
from model import SecretDao
from db.check_secret import check_secret

class TestCheckSecret():
    def test_check_when_date_is_old(self):
        foo = SecretDao(2,"foo","foo",datetime.now(), datetime(1984,5,5,2,2,0),5)
        expected = False
        actual = check_secret(foo)
        assert expected == actual

    def test_check_when_all_good(self):
        foo = SecretDao(2,"foo","foo",datetime.now(), datetime(2055,5,5,2,2,0),5)
        expected = True
        actual = check_secret(foo)
        assert expected == actual

    def test_check_when_no_data_given(self):
        with pytest.raises(Exception) as exc_info:
            check_secret(None)
            assert exc_info == "No data given"

    def test_when_only_two_visit_allowed(self):
        foo = SecretDao(2,"foo","foo",datetime.now(), datetime(2055,5,5,2,2,0),2)
        expected = True
        actual = check_secret(foo)
        assert expected == actual

    def test_when_last_visit(self):
        foo = SecretDao(2,"foo","foo",datetime.now(), datetime(2055,5,5,2,2,0),1)
        expected = False
        actual = check_secret(foo)
        assert expected == actual
        
    def test_check_when_visit_is_zero(self):
        foo = SecretDao(2,"foo","foo",datetime.now(), datetime(2055,5,5,2,2,0),0)
        expected = False
        actual = check_secret(foo)
        assert expected == actual
from unittest.mock import Mock, patch
import pytest
from service.update_secret_service import update_secret
from model import SecretDao
class TestUpdate_secret_service():
    def test_when_check_successful(self):
        with patch(
    "service.update_secret_service.update_secret_in_db"
           ) as mock_update,patch(
               "service.update_secret_service.check_secret", return_value=True
               ) as mock_check:
              update_secret(None,None)
              mock_check.assert_called_once()
              mock_update.assert_called_once()

    def test_when_check_failed(self):
        with patch(
    "service.update_secret_service.delete_secret"
           ) as mock_delete,patch(
               "service.update_secret_service.check_secret", return_value=False
               ) as mock_check:
              foo = SecretDao(1,"foo", "bar", None, None, 1)
              update_secret(foo,None)
              mock_check.assert_called_once()
              mock_delete.assert_called_once()

    def test_when_delete_query_failed(self):
        with patch(
    "service.update_secret_service.delete_secret", return_value=Exception("foo")
           ) as mock_delete,patch(
               "service.update_secret_service.check_secret", return_value=False
               ) as mock_check:
              foo = SecretDao(1,"foo", "bar", None, None, 1)
              with pytest.raises(Exception) as exc_info:
                    update_secret(foo,None)
                    assert exc_info == "foo"
                    mock_check.assert_called_once()
                    mock_delete.assert_called_once()
                    
    def test_when_update_query_failed(self):
        with patch(
    "service.update_secret_service.update_secret_in_db", return_value=Exception("foo")
           ) as mock_update,patch(
               "service.update_secret_service.check_secret", return_value=True
               ) as mock_check:
              foo = SecretDao(1,"foo", "bar", None, None, 1)
              with pytest.raises(Exception) as exc_info:
                    update_secret(foo,None)
                    assert exc_info == "foo"
                    mock_check.assert_called_once()
                    mock_update.assert_called_once()



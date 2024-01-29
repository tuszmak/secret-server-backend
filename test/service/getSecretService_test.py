import pytest
from unittest.mock import patch
from service.get_secret_service import get_secret_by_hash

class TestGetSecretService():

    def test_run_all_methods(self):
        with patch(
        "service.get_secret_service.get_secret_from_db"
               ) as mock_fetch,patch(
                   "service.get_secret_service.to_secret_dao"
                   ) as mock_dao, patch(
                           "service.get_secret_service.decrypt_secret", return_value={"secret": "bar"}
                           ) as mock_decrypt:
            get_secret_by_hash({"secret": "foo"}, None)
            mock_fetch.assert_called_once()
            mock_dao.assert_called_once()
            mock_decrypt.assert_called_once()

    def test_fail(self):
        with patch(
        "service.get_secret_service.get_secret_from_db"
               ) as mock_fetch,patch(
                   "service.get_secret_service.to_secret_dao"
                   ) as mock_dao, patch(
                           "service.get_secret_service.decrypt_secret", side_effect=Exception("foo")
                           ) as mock_decrypt:
            with pytest.raises(Exception) as exc_info:
                get_secret_by_hash({"secret": "foo"}, None)
                assert exc_info == "foo"
            mock_fetch.assert_called_once()
            mock_dao.assert_called_once()
            mock_decrypt.assert_called_once()
                              
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
                       "service.get_secret_service.update_secret"
                       ) as mock_update, patch(
                           "service.get_secret_service.decrypt_secret", return_value="bar"
                           ) as mock_decrypt:
            expected = "bar"
            actual = get_secret_by_hash("foo", None)
            assert expected == actual
            mock_fetch.assert_called_once()
            mock_dao.assert_called_once()
            mock_update.assert_called()
            mock_decrypt.assert_called_once()

    def test_fail(self):
        with patch(
        "service.get_secret_service.get_secret_from_db"
               ) as mock_fetch,patch(
                   "service.get_secret_service.to_secret_dao"
                   ) as mock_dao, patch(
                       "service.get_secret_service.update_secret"
                       ) as mock_update, patch(
                           "service.get_secret_service.decrypt_secret", side_effect=Exception("foo")
                           ) as mock_decrypt:
            with pytest.raises(Exception) as exc_info:
                get_secret_by_hash("foo", None)
                assert exc_info == "foo"
            mock_fetch.assert_called_once()
            mock_dao.assert_called_once()
            mock_update.assert_called()
            mock_decrypt.assert_called_once()
                              
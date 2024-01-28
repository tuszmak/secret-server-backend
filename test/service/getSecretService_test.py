import pytest
from service.getSecretService import get_secret_by_hash
from unittest.mock import Mock, patch

class Test_Get_Secret_Service():
    def test_run_all_methods(self):
        with patch(
        "service.getSecretService.getSecretFromDb"
               ) as mock_fetch,patch(
                   "service.getSecretService.to_secret_dao"
                   ) as mock_dao, patch(
                       "service.getSecretService.update_secret"
                       ) as mock_update, patch(
                           "service.getSecretService.decryptSecret", return_value="bar"
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
        "service.getSecretService.getSecretFromDb"
               ) as mock_fetch,patch(
                   "service.getSecretService.to_secret_dao"
                   ) as mock_dao, patch(
                       "service.getSecretService.update_secret"
                       ) as mock_update, patch(
                           "service.getSecretService.decryptSecret", side_effect=Exception("foo")
                           ) as mock_decrypt:
                with pytest.raises(Exception) as exc_info:
                    get_secret_by_hash("foo", None)
                    assert exc_info == "foo"
                mock_fetch.assert_called_once()
                mock_dao.assert_called_once()
                mock_update.assert_called()
                mock_decrypt.assert_called_once()
                
                
import pytest
from service.deleteSecretService import delete_secret
from unittest.mock import Mock, patch

class Test_Delete_Secret():
    @patch("service.deleteSecretService.delete_secret_from_db")
    def test_use_delete_method(self, mock_delete_secret: Mock):
        delete_secret("foo", None)
        mock_delete_secret.assert_called_once()
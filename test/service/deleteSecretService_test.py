from unittest.mock import Mock, patch
from service.delete_secret_service import delete_secret

class TestDeleteSecret():

    @patch("service.delete_secret_service.delete_secret_from_db")
    def test_use_delete_method(self, mock_delete_secret: Mock):
        delete_secret("foo", None)
        mock_delete_secret.assert_called_once()

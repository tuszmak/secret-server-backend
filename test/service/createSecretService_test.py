from model import SecretData
from datetime import datetime
import pytest
from service import createSecretService
from unittest.mock import patch, Mock

class Test_CreateSecretService():
    def test_create_secret_without_text(self):
        foo = SecretData("", 5, datetime.now())
        with pytest.raises(Exception):
            createSecretService.create_secret_dao(foo)
    def test_create_secret_without_zero_visits(self):
        foo = SecretData("foo", 0, datetime.now())
        with pytest.raises(Exception):
            createSecretService.create_secret_dao(foo)
    def test_create_secret_without_exp_date(self):
        foo = SecretData("foo", 5, None)
        with pytest.raises(Exception):
            createSecretService.create_secret_dao(foo)
    def test_create_secret_with_no_data(self):
        foo = SecretData("", 0, None)
        with pytest.raises(Exception):
            createSecretService.create_secret_dao(foo)
    @patch(target="service.createSecretService.createSecret")
    def test_creating_data(self, mock_createSecret : Mock):
        foo = {
            "expiryDate": datetime.now(),
            "secret": "foo",
            "numberOfVisits": 5
        }
        createSecretService.create_secret_dao(foo,None)
        mock_createSecret.assert_called_once()
    @patch(target="service.createSecretService.createSecret")
    def test_creating_data_fail(self, mock_createSecret : Mock):
        foo = {
            "expiryDate": datetime.now(),
            "secret": "foo",
            "numberOfVisits": 5
        }
        createSecretService.create_secret_dao(foo,None)
        mock_createSecret.assert_called_once()
    

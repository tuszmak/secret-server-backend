from datetime import datetime
from unittest.mock import patch, Mock
import pytest
from model import SecretData
from service import create_secret_service

class TestCreateSecretService():
    
    def test_create_secret_without_text(self):
        foo = SecretData("", 5, datetime.now())
        with pytest.raises(Exception):
            create_secret_service.create_secret_dao(foo, None)

    def test_create_secret_without_zero_visits(self):
        foo = SecretData("foo", 0, datetime.now())
        with pytest.raises(Exception):
            create_secret_service.create_secret_dao(foo, None)

    def test_create_secret_without_exp_date(self):
        foo = SecretData("foo", 5, None)
        with pytest.raises(Exception):
            create_secret_service.create_secret_dao(foo, None)

    def test_create_secret_with_no_data(self):
        foo = SecretData("", 0, None)
        with pytest.raises(Exception):
            create_secret_service.create_secret_dao(foo, None)

    @patch(target="service.create_secret_service.create_secret")
    def test_creating_data(self, mock_createSecret : Mock):
        foo = {
            "expiryDate": datetime.now(),
            "secret": "foo",
            "numberOfVisits": 5
        }
        create_secret_service.create_secret_dao(foo,None)
        mock_createSecret.assert_called_once()

    @patch(target="service.create_secret_service.create_secret")
    def test_creating_data_fail(self, mock_createSecret : Mock):
        foo = {
            "expiryDate": datetime.now(),
            "secret": "foo",
            "numberOfVisits": 5
        }
        create_secret_service.create_secret_dao(foo,None)
        mock_createSecret.assert_called_once()

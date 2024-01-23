import pytest
from base64 import b64encode, b64decode
from db.get_secret import getSecretFromDb
from unittest.mock import patch, Mock
from encrypt.encryption import decryptSecret,encryptSecret


class Test_Encryption():
    # EncryptSecret tests
    def test_encrypt_secret(self):
        foo = "secret"
        expected = b64encode(foo.encode("ascii")).decode("ascii")
        actual = encryptSecret(foo)
        assert expected == actual
    #decryptSecret tests
    #The input params are redundant, because I don't test the db queries here.
    def test_decrypt_with_empty_string(self):
        expected = None
        actual = decryptSecret("")
        assert expected == actual

    def test_decrypt_with_none(self):
        expected = None
        actual = decryptSecret(None)
        assert expected == actual

    
    def test_decrypt_with_number(self):
        with pytest.raises(Exception) as exc_info:
            decryptSecret(5)
            assert exc_info == "This data is not Base64!"

    def test_decrypt_with_not_base64(self):
        with pytest.raises(Exception) as exc_info:
            decryptSecret("foo")
            assert exc_info == "This data is not Base64!"

    def test_decrypt_with_base64(self):
        expected = {"secret": "asd"}
        actual = decryptSecret("YXNk")
        assert expected == actual


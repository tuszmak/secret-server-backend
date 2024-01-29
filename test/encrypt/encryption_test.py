from base64 import b64encode
import pytest
from encrypt.encryption import decrypt_secret,encrypt_secret


class Test_Encryption():
    # EncryptSecret tests
    def test_encrypt_secret(self):
        foo = "secret"
        expected = b64encode(foo.encode("ascii")).decode("ascii")
        actual = encrypt_secret(foo)
        assert expected == actual
    #decryptSecret tests
    #The input params are redundant, because I don't test the db queries here.
    def test_decrypt_with_empty_string(self):
        expected = None
        actual = decrypt_secret("")
        assert expected == actual

    def test_decrypt_with_none(self):
        expected = None
        actual = decrypt_secret(None)
        assert expected == actual

    
    def test_decrypt_with_number(self):
        with pytest.raises(Exception) as exc_info:
            decrypt_secret(5)
            assert exc_info == "This data is not Base64!"

    def test_decrypt_with_not_base64(self):
        with pytest.raises(Exception) as exc_info:
            decrypt_secret("foo")
            assert exc_info == "This data is not Base64!"

    def test_decrypt_with_base64(self):
        expected = {"secret": "asd"}
        actual = decrypt_secret("YXNk")
        assert expected == actual

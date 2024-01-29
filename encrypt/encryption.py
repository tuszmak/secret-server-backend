from base64 import b64encode, b64decode
import shortuuid

def encrypt_secret(secret: str):
    encoded_string = b64encode(secret.encode("ascii"))
    return encoded_string.decode("ascii")

def generate_link():
    return shortuuid.uuid()

def decrypt_secret(secret: str):
    if(secret != "" and secret is not None):
        try:
            secret_bytes = b64decode(secret.encode())
            decoded_secret = secret_bytes.decode("ascii")
        except:
            raise Exception("This data is not Base64!")
        response_data = {"secret": decoded_secret}
        return response_data
    return None

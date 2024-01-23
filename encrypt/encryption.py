import shortuuid
from base64 import b64encode, b64decode

def encryptSecret(secret: str):
     foo = b64encode(secret.encode("ascii"))
     return foo.decode("ascii")

def generateLink():
    return shortuuid.uuid()

def decryptSecret(secret: str):
    if(secret != "" and secret!= None):
        try:
            secretBytes = b64decode(secret.encode())
            decodedSecret = secretBytes.decode("ascii")
        except:
            raise Exception("This data is not Base64!")
        responseData = {"secret": decodedSecret}
        return responseData
    return None

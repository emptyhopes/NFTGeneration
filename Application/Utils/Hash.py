import hashlib
import base64


class Hash:
    decode = "latin1"
    encode = "UTF-8"

    def Decode (string):
        return string.decode(Hash.decode)

    def Encode (string):
        return string.encode(Hash.encode)

    def Encrypt (string):
        return hashlib.sha256(string)

    def Hex (string):
        return string.hexdigest()
    
    def GetHash(files):
        string = b""

        for file in files: 
            with open(file, "rb") as image:
                string = string + base64.b64encode(image.read())

        decode = Hash.Decode(string)
        encode = Hash.Encode(decode)
        hash = Hash.Encrypt(encode)
        hex = Hash.Hex(hash)

        return hex
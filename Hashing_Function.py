import hashlib

def hashText(text):
    byte_obj = (str(text)).encode()
    
    hash_obj = hashlib.sha3_512(byte_obj)
    
    output = hash_obj.hexdigest()
    
    return output


if __name__ == "__main__":
    text = "Test"
    print(hashText(text))
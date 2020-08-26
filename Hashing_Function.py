import hashlib

def hashText(text):
    byte_obj = (str(text)).encode()
    
    hash_obj = hashlib.sha3_512(byte_obj)
    
    output = hash_obj.hexdigest()
    
    return output


if __name__ == "__main__":
    text = "Test"
    print(hashText(text))
    
print(var)
for r in range(0, len(list)):
    print(f" [{r}] - {list[r]}")

print("[99] - Exit")
input = input("Enter option: ")

return input
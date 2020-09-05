##Sprint Week 3: Digital Signatures
#need to revise, some errors present.
#Yet to make it such that it processes each individual letter instead of a long string of text. Is this necessary? I understand that creating the keys requires effort of separately
#encoding the letters of a message, but all this is doing is running the already made keys through a pow() function, so why even bother???

import hashlib

#A function to take a message and add a signature.
def gen_signature(message, d, n):
    #convert to dec
    d = int(d, 16)
    n = int(n, 16)
    message = str(message)

    #Take first 16 characters of message:
    M = message[0:16]
    hashed_m = hashlib.sha3_512(M.encode()).hexdigest()

    #make signed message:
    signed_m = b"sha3_512".hex() + hashed_m

    #split message
    sign1 = signed_m[0:32]
    sign2 = signed_m[32:]

    #final1 contains the hash function and some of the message; final2 contains the other part of the message
    #Encoding using asymmetric keys
    final1 = hex(pow(int(sign1, 16), d, n))
    final2 = hex(pow(int(sign2, 16), d, n))

    #remove the 0x in front:
    final1 = final1[2:]
    if len(final1) <32:
        final1 = final1.zfill(32)

    final2 = final2[2:]
    if len(final2) <32:
        final2 = final2.zfill(32)

    #final signed combines the different parts of the message a
    final_signed = final1 + final2

    #Return the final signed message and the hashed message (to compare)
    return [message, hashed_m, final_signed]

def check_signature(message, final_signed, e, n):
    e = int(e, 16)
    n = int(n, 16)

    #Split into parts first.
    final1 = final_signed[0:32]
    final2 = final_signed[32:]

    #Decodes parts   
    D1 = hex(pow(int(final1, 16), e, n))
    D2 = hex(pow(int(final2, 16), e, n))

    #Remove the 0x
    D1 = D1[2:]
    D2 = D2[2:]

    #Takes the padding and prints it
    padding = bytes.fromhex(D1[0:16]).decode()
    print(f"padding = {padding}")

    #Takes the first 16 digits of the message 
    M = message[0:16]
    
    #hashes the M using the padding recieved from the sender
    #eval is used to str is treated as code.
    hash_m = eval(f"hashlib.{padding}(M.encode()).hexdigest()")
    return hash_m



#Testing
if __name__ == "__main__":

    #Test gen_signature using one message, d and n values
    print(gen_signature("hi", '4d87c9ba199f52ad3fbc88251ab44fff', '89c543ada411350b01c171a81f91ba1f'))

    #Test check_signature giving it an encoded message, e and n values
    print(check_signature("hi","47acf1e1a3bfb632101c21a8c7cc252c773396de83bbaf276e5719bce3c84845", '27ff', '89c543ada411350b01c171a81f91ba1f'))

    #If it works, the hash of the original function should match the hash of the recieved message using the padding.

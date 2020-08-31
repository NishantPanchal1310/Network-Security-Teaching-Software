##Sprint Week 3: Digital Signatures
#need to revise, some errors present.

import hashlib

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

    #final1 contains the hash function and some of the message
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

    final_signed = final1 + final2
    return [final_signed, hashed_m]

def check_signature(final_signed, e, n):
    e = int(e, 16)
    n = int(n, 16)

    #Split into parts first.
    part1 = final_signed[0:32]
    part2 = final_signed[32:]

    #Decodes parts   
    D1 = hex(pow(int(part1, 16), e, n))
    D2 = hex(pow(int(part2, 16), e, n))

    #Remove the 0x
    D1 = D1[2:]
    D2 = D2[2:]

    #Takes the padding
    padding = bytes.fromhex(D1[0:16]).decode()
    print(f"padding = {padding}")
    Hash = D1[16:] + D2
    print(f"Hash from signed message: {Hash}")



#Testing
if __name__ == "__main__":

    #Test gen_signature
    print(gen_signature("hi", '4d87c9ba199f52ad3fbc88251ab44fff', '89c543ada411350b01c171a81f91ba1f'))

    #Test check_signature
    check_signature("47acf1e1a3bfb632101c21a8c7cc252c773396de83bbaf276e5719bce3c84845", '27ff', '89c543ada411350b01c171a81f91ba1f')
    #There's something wrong with my message slicing since we are using a different hash function
    #below is the 16 characters of the message that matches.
    print(len("154013cb8140c753"))



##Sprint Week 3: Digital Signatures
#need to revise, some errors present.
#Yet to make it such that it processes each individual letter instead of a long string of text. Is this necessary? I understand that creating the keys requires effort of separately
#encoding the letters of a message, but all this is doing is running the already made keys through a pow() function, so why even bother???

import hashlib

#A function to take a message and add a signature.
def gen_signature(message, d, n):
    #convert to int
    #convert to int
    d = int(d)
    n = int(n)
    message = str(message)

    #Take first 16 characters of message:
    M = message[0:16]
    hashed_m = hashlib.sha3_512(M.encode()).hexdigest()

    #make signed message:
    signed_m = b"sha3_512".hex() + hashed_m

    #split message and only take first 64 digits of hash
    signed_list =  [signed_m[i:i+32] for i in range(0, len(signed_m), 32)]

    #final1 contains the hash function and some of the message; final2 contains the other part of the message
    #Encoding using asymmetric keys
    final_list = []
    for i in signed_list:
        i = hex(pow(int(i, 16), d, n))
        i = i[2:]
        final_list.append(i)

    #final signed combines the different parts of the message a
    final_signed = "".join(final_list)

    output = message + "0x" + final_signed

    #Return the final signed message and the hashed message (to compare)
    return output

def check_signature(output, e, n):
    #split incoming signature into message and signed message, and assign to respective variables
    output = output.split("0x")
    message = output[0]
    final_signed = output[1]


    #Make sure it is an integer
    e = int(e)
    n = int(n)

    #Split into parts first.
    final_signed_list = [final_signed[i:i+32] for i in range(0, len(final_signed), 32)]

    #Decodes parts 
    decode_message_list = []
    for i in final_signed_list:
        i = hex(pow(int(i, 16), e, n))
        i = i[2:]
        decode_message_list.append(i)

    D1 = decode_message_list[0]
 
        
    #Takes the padding and prints it
    padding = bytes.fromhex(D1[0:16]).decode()
    print(f"padding = {padding}")

    #Takes the first 16 digits of the message 
    M = message[0:16]

    #hashes the M using the padding recieved from the sender
    #eval is used to str is treated as code.
    hash_m = eval(f"hashlib.{padding}(M.encode()).hexdigest()")

    #To compare:
    check_message = "".join(decode_message_list)
    print(check_message[16:])

    return hash_m



#Testing
if __name__ == "__main__":

    #Test gen_signature using one message, d and n values
    output = gen_signature("hi", '103055607260039020463150134675226513407', '183128490582356739098389207284479801887')
    print(output)

    #Test check_signature giving it an encoded message, e and n values
    #Some weird bug where the 2 element in list is different but the rest matches???
    print(check_signature(output, '10239', '183128490582356739098389207284479801887'))
    

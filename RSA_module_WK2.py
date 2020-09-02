import hashlib
import base64
import rsa


##Experimental
#Generates public (e,n) and private (d,n) keys [128bit]
def gen_key():
    (pubkey, privkey) = rsa.newkeys(128)

    #converts public key into string
    public_tuple = str(pubkey)
    pub_key = str(public_tuple[9:])
    pub_key = pub_key[:-1]
    pub_key = pub_key[1:]
    pub_key = pub_key.split(", ")

    #converts private key into string
    priv_tuple = str(privkey)
    priv_key = str(priv_tuple[9:])
    priv_key = priv_key[:-1]
    priv_key = priv_key[2:]
    priv_key = priv_key.split(", ")
    
    #Convert keys to int
    n_key = int(pub_key[0])
    d_key = int(priv_key[2])
    e_key = int(pub_key[1])
    
    #convert int to hex
    n_key = hex(n_key)
    d_key = hex(d_key)
    e_key = hex(e_key)

    #keys are given as [<public key>] - have to modify to return as int not str, purely testing.
    keys = "n: " + str(n_key) + "\nd: " + str(d_key) + "\ne value: " + str(e_key)
    return keys
    #Instead of return directly interact with students class
    #Note, the keys returned are in hexadecimal


#Message as string, e and n as str and in base 16
def RSA_encode(message, e, n):
    # Encoding each individual character
    message_split = [(message[i:i+16]) for i in range(0, len(message), 16)] # Spliting str into list
    message_split_bytes = []
    message_split_hex = []
    message_split_int = []

    for i in message_split:
        message_split_bytes.append(i.encode()) # Convert to bytes
        
    for i in message_split_bytes:
        message_split_hex.append(i.hex()) # Convert to hexadecimal

    for i in message_split_hex:
        message_split_int.append(int(i, 16)) # Convert to int

    # Encoding
    cipher = []

    for i in message_split_int:
        cipher_n = pow(i, e, n) # Put through function
        cipher.append(hex(cipher_n))

    output = ""

    for i in cipher:
        output += i
    
    return output


def RSA_decode(cipher, d, n):
    #converts hexadecimal to base 10
    d = int(d, 16)
    n = int(n, 16)

    #lists that temp. store each step of cipher
    C = []
    N = []
    decoding_message_hex = []
    decoding_message_bytes = []
    decoded_message = []

    for i in cipher:
        C.append(int(i, 16)) # Convert to number
        
    for i in C:
        N.append(pow(i, d, n)) # Reverse through function

    for i in N:
        decoding_message_hex.append(hex(i)) # Convert N to hexidecimal

    for i in decoding_message_hex:
        decoding_message_bytes.append(bytes.fromhex(i[2:])) # Convert to byte code

    for i in decoding_message_bytes:
        decoded_message.append(i.decode()) # Decode byte code

    output = ''.join(decoded_message) # combining list into single string
    return output #output is returned as string.


#Test RSA_encode and RSA_decode with keys that are given in hexadecimal
if __name__ == "__main__":
    print(gen_key())
    print(RSA_encode("wassup", '48055fe1', '6a1445eac29d8b07e5dcb688e3854993'))
    ciphered_m = RSA_encode("wassup", '48055fe1', '6a1445eac29d8b07e5dcb688e3854993')
    print(RSA_decode(ciphered_m,'57d16f9acad8550584e78d0ca2f2e839','6a1445eac29d8b07e5dcb688e3854993'))

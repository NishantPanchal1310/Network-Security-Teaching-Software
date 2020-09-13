import hashlib
import base64
import rsa
#from RSA_Algorithm import *
#from Prime_Number_Generator import *



#Generates public (e,n) and private (d,n) keys [512bit]
#Alternate approach but relies on the use of rsa import.
def gen_key():
    (pubkey, privkey) = rsa.newkeys(512)

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

    #keys are returned as [n, d, e] in decimal
    keys = [n_key, d_key, e_key]
    return keys
    #Instead of return directly interact with students class
# Generates keys
'''
def gen_key(bits):
    gen_prime(bits)
    keys = generate_key_with_custom_RSA_alogrithm(bits)
    return keys # Can be treated as a list
'''
#Message as string, e and n as str and in base 10
def RSA_encode(message, e, n):
    #Breaking long message into blocks of 50
    message_split = [message[i:i+16] for i in range(0, len(message), 16)]# Spliting str into list
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
        cipher_n = pow(i, int(e), int(n)) # Put through function
        cipher.append(hex(cipher_n))
        
    #joining back the blocks as str for simplicity
    cipher  = "".join(cipher)
    return cipher


#Decodes the cipher when given d and n. d and n are given as decimal. The cipher is the string.
def RSA_decode(cipher, d, n):   
    #Break up cipher into list of blocks of messages 50 char in length.
    cipher = cipher.split('0x')
    cipher = cipher[1:]

    #lists that temp. store each step of cipher
    C = []
    N = []
    decoding_message_hex = []
    decoding_message_bytes = []
    decoded_message = []

    for i in cipher:
        C.append(int(i, 16)) # Convert to number
        
    for i in C:
        N.append(pow(i, int(d), int(n))) # Reverse through function

    for i in N:
        decoding_message_hex.append(hex(i)) # Convert N to hexidecimal

    for i in decoding_message_hex:
        decoding_message_bytes.append(bytes.fromhex(i[2:])) # Convert to byte code

    for i in decoding_message_bytes:
        decoded_message.append(i.decode()) # Decode byte code

    output = ''.join(decoded_message) # combining list into single string
    return output #output is returned as string.


#Test RSA_encode and RSA_decode with keys that are given in hexadecimal
#Testing is 128bit keys so it is easy to follow
if __name__ == "__main__":
    # Key are generated using the RSA_Alogrithm
    print(gen_key())

    #The follow code tests the encoding and decoding of text.
    ciphered_m = RSA_encode("hello djf alkejfklajfdlkajrflkajflkeajfaeiltfjaweskjfskl jtlkjsekljz", "65537", "11723087253621038540617270065495609242591710500556289890700176949875148684480984805819907599320837558245210193280379774462990384004325702123948704997207601")
    print("encoded message: " + ciphered_m)
    print("Decoded: " + RSA_decode(ciphered_m, "7797623015393568702604453006623504251080425471722077435882053093656369396826802935591468805848897290139059477614451217656187882589768924456469723679931265","11723087253621038540617270065495609242591710500556289890700176949875148684480984805819907599320837558245210193280379774462990384004325702123948704997207601"))

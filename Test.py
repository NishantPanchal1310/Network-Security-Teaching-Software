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


RSA_decode(RSA_encode("Hello I like anime", 77791, 109089), 635478271, 109089)

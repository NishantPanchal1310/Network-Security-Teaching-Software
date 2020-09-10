import hashlib

#Give d and n as int in base 10
def gen_sig(message, d, n):
    hash_list = []

    #Creating list of hashed 50 char length messages
    message_list = [message[i:i+50] for i in range(0, len(message), 50)]
    for i in message_list:
        hash_list.append(hashlib.sha3_512(i.encode()).hexdigest())
    
    #Add the padding
    signed_m = b"sha3_512".hex() + "".join(hash_list)

    #need to break it up into 32 byte pieces and feed it through the power function individually
    pieces_32 = [signed_m[i:i+32] for i in range(0, len(signed_m), 32)]
    
    #encoding the 32 byte messages
    encode_m = []
    for i in pieces_32:
        i_encoded = hex(pow(int(i, 16), d, n))
        encode_m.append(i_encoded[2:])

    #note, each 32 byte long message becomes 128 bytes long after feeding it through power function
    output = message + "0x"+ "".join(encode_m)
    return output

def check_sig(output, e, n):
    output_split = output.split("0x")
    encode_m = output_split[1]
    
    #Since after RSAing the message the 32 bytes become 128, this converts 128 bytes back to the og 32 bytes.
    pieces_128 = [encode_m[i:i+128] for i in range(0, len(encode_m), 128)]
   
    decoded_m = []
    for i in pieces_128:
        i_decoded = hex(pow(int(i, 16), e, n))
        decoded_m.append(i_decoded[2:])

    #Original message with padding produced from the output variable given to the function.
    signed_m = "".join(decoded_m)
    
    #padding
    padding  = bytes.fromhex(signed_m[0:16]).decode()
    print(f'padding = {padding}')
    
    #Hash message as before:
    message = output_split[0]
    message_list = [message[i:i+50] for i in range(0, len(message), 50)]
    hash_list = []
    for i in message_list:
        i_hashed = eval(f"hashlib.{padding}(i.encode()).hexdigest()")
        hash_list.append(i_hashed)

    hashed_m = b"sha3_512".hex() + "".join(hash_list)
    print("Original signm: " + signed_m)
    print("Hashed message: " + hashed_m)

    

if __name__ == "__main__":
    output = gen_sig("hello", 383913587312119444973630894662724647649092038597280444459286303313546867935562968831856083151629726348794881837431695143612710809789817532782515965167681, 7939584970550448742580261263335747943508534216961176550498026652022695204209765530457332763718222257951450449100284952436042956675481597109576749730866491)
    print(output)
    check_sig(output, 65537, 7939584970550448742580261263335747943508534216961176550498026652022695204209765530457332763718222257951450449100284952436042956675481597109576749730866491)

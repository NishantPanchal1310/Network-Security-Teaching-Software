import hashlib

#Give d and n as int in base 10
def gen_sig(message, d, n):
    hash_list = []



    hash_list = hashlib.sha3_512(message.encode()).hexdigest()
    
    #Add the padding
    signed_m = b"sha3_512".hex() + "".join(hash_list)

    #need to break it up into 128 byte pieces and feed it through the power function individually
    pieces_128 = [signed_m[i:i+128] for i in range(0, len(signed_m), 128)]
    
    #encoding the 128 byte messages
    encode_m = []
    for i in pieces_128:
        i_encoded = hex(pow(int(i, 16), d, n))
        i_encoded = i_encoded[2:]

        #Make sure the length of each element in the encoded list is 128 bytes long.
        if len(i_encoded) < 128:
            i_encoded = i_encoded.zfill(128)

        encode_m.append(i_encoded)

    #note, each 32 byte long message becomes 128 bytes long after feeding it through power function
    output = message + "0x"+ "".join(encode_m)
    return output


def check_sig(output, e, n):
    try:
        output_split = output.split("0x")
        encode_m = output_split[1]
        
        #Since after RSAing the message each of the individual elements are 128
        pieces_128 = [encode_m[i:i+128] for i in range(0, len(encode_m), 128)]
    
        decoded_m = []
        for i in pieces_128:
            i_decoded = hex(pow(int(i, 16), e, n))
            decoded_m.append(i_decoded[2:])

        #Original message with padding produced from the output variable given to the function.
        signed_m = "".join(decoded_m)
        
        #padding
        padding  = bytes.fromhex(signed_m[0:16]).decode()
        print(f'padding = {padding}' + "\n")
        
        #Hash message as before:
        message = output_split[0]

        hashed_m = eval(f"hashlib.{padding}(message.encode()).hexdigest()")

        #Take out b"sha3_512".hex() (which is the first 16 bytes)
        print("Message from signature: " + "\n" + signed_m[16:] + "\n")
        print("Hashing Message using padding: " + "\n" + hashed_m + "\n")

        #Check that they match
        if signed_m[16:] == hashed_m:
            print("It matches.")
            print("You have recieved it from a correct sender.")
        elif signed_m[16:] != hashed_m:
            print("It does not match.")
    except:
        print("It does not match.")

    

##Testing 
if __name__ == "__main__":
    #This produces a signed message
    output = gen_sig("ghehrhgh ehe ehrh fheasejfhsadfhjefkjsehfkjaseb ehj hekjakj nenjk nejnejkfhejkfah jhhjkhjhlkj fsdkfjklejflkaj dfkjsklfjkeja;dkjfalkenfnake kdjf;lakejrflksadfnalekn", 383913587312119444973630894662724647649092038597280444459286303313546867935562968831856083151629726348794881837431695143612710809789817532782515965167681, 7939584970550448742580261263335747943508534216961176550498026652022695204209765530457332763718222257951450449100284952436042956675481597109576749730866491)
    print(output)
    #Take the output and feed it through the checking function
    check_sig(output, 65537, 7939584970550448742580261263335747943508534216961176550498026652022695204209765530457332763718222257951450449100284952436042956675481597109576749730866491)

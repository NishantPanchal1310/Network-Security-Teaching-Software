#SPRINT WEEK 1: BUILD 1.0
import hashlib
import base64
import pickle

    
#Hashes message with sha3_512      
def hashText(text):
    byte_obj = (str(text)).encode()
    hash_obj = hashlib.sha3_512(byte_obj)
    output = hash_obj.hexdigest()
    return output
    
#Reads pickle file with a given name and returns whatever is stored
def readFilePk(filename):
    try:
        pickle_in = open(str(filename),"rb")
        message_get = pickle.load(pickle_in)
        pickle_in.close()
        return message_get
    except:
        return "File not found"

#save given text to a pickle file of a given name
def saveFilePk(text, filename):
    pickle_out = open(str(filename),"wb")
    pickle.dump(text, pickle_out)
    pickle_out.close()
        



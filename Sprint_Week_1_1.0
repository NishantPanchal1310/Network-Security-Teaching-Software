#SPRINT WEEK 1: BUILD 1.0
import hashlib
import base64
import pickle

#Create class of message
class Message:
    def __init__(self, text = " ", filename = "Not found", message_list = [], hashed_result = ""):
        self.text = text 
        self.filename = filename
        self.message_list = message_list
        self.hashed_result = hashed_result
    
    #adds text into message_list directly
    def addText(self, user_input):
        self.message_list.append(user_input)
    
    #Hashes message with md5
    def hashMessage(self, text):
        #convert to bytes
        to_byte = text.encode()
        #convert to hash
        to_hash = hashlib.md5(to_byte)
        #store hashed result as hex
        self.hashed_result = to_hash.hexdigest()
        return self.hashed_result
    
    #Reads message_list in a pickle file with a given name and returns message_list
    def readFilePk(self, filename):
        pickle_in = open(str(filename),"rb")
        self.message_list = pickle.load(pickle_in)

        pickle_in.close()
        return self.message_list

    #save message_list to a pickle file of a given name
    def saveFilePk(self, filename):
        pickle_out = open(str(filename),"wb")
        pickle.dump(self.message_list, pickle_out)
        pickle_out.close()


'''
##To test saveFilePk() and readFilePk()

#creates new object
m_test = Message("test2") 
#using addText, append message of object into message_list
m_test.addText(m_test.text)
#save message_list to a pickle file known as "dictpickle" (to add user input for any name)
m_test.saveFilePk("dictpickle")
#Retrieve message_list and then print it
print(m_test.readFilePk("dictpickle"))
'''

'''
#2 lines to test hashMessage()
newmessage = Message("yo wassup")
print(newmessage.hashMessage(newmessage.text))
'''

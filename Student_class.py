#from Prime_Number_Generator import gen_prime
#from RSA_Algorithm import generate_key_with_custom_RSA_alogrithm
from Functions_Module_WK1 import *


#Class for students is generated in order to use it for storing keys.
class students():
    def __init__(self, name, pubkey, privkey, nValue, password):
        self.name = name
        self.pubkey = int(pubkey)
        self.privkey = int(privkey)
        self.nValue = int(nValue)
        self.password = password
    
    
   # These methods return the respective values as given in the name
    def get_name(self):
        return self.name
    def get_pubkey(self):
        return self.pubkey
    def get_privkey(self):
        return self.privkey
    def get_nValue(self):
        return self.nValue
    def get_password(self):
        return self.password
    
    # These methods can edit the values for keys.
    def edit_pubkey(self, new_key):
        self.pubkey = int(new_key)
    def edit_privkey(self, new_key):
        self.privkey = int(new_key)
    def edit_nValue(self, new_key):
        self.nValue = int(new_key)
    def edit_password(self, password):
        self.password = password

# function is used to create a new student.
def new_student(name, n, d, e, password):
    new_student = students(name, e, d, n, password)
    return new_student

#Used to open and take out the student objects from the file containing it.
def open_student_database():
    try:
        contents = readFilePK("studentData")
        return contents
    except:
        contents = []
        return contents

#This is to save a list of student objects back into the pickle file.
def save_student_database(listOfObjects):
    saveFilePK(listOfObjects,"studentData")
    
# A method to search for a student using their name by checking every object in a list.
def search_by_name(name, listOfObjects):
    for i in range(0, len(listOfObjects)):
        if (listOfObjects[i].get_name()).lower() == name.lower():
            return i
        

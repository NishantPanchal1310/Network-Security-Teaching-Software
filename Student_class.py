from Prime_Number_Generator import gen_prime
from RSA_Algorithm import generate_key_with_custom_RSA_alogrithm
from Functions_Module_WK1 import *

class students():
    def __init__(self, name, pubkey, privkey, n):
        self.name = name
        self.pubkey = pubkey
        self.privkey = privkey
        self.nValue = n
    
    def get_name(self):
        return self.name
    def get_pubkey(self):
        return self.pubkey
    def get_privkey(self):
        return self.privkey
    def get_nValue(self):
        return self.nValue
    
    def edit_pubkey(self, new_key):
        self.pubkey = new_key
    def edit_privkey(self, new_key):
        self.privkey = new_key
    def edit_nValue(self, new_key):
        self.nValue = new_key
    
def new_student(name, e, d, n):
    new_student = students(name, e, d, n)
    return new_student

def open_student_database():
    try:
        contents = readFilePK("studentData")
        return contents
    except:
        contents = []
        return contents

def save_student_database(listOfObjects):
    saveFilePK(listOfObjects,"studentData")
    
def search_by_name(name, listOfObjects):
    x = []
    for objects in listOfObjects:
        if objects.name == "name":
            return x.append(objects)
    
    return x
        
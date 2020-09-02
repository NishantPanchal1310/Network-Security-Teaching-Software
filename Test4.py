from Student_class import * 
from RSA_module_WK2 import gen_key

studentClassList = open_student_database()    

new_keys = gen_key(16)

print(new_keys[0])

print(studentClassList)
print(studentClassList[0].pubkey)
##Incomplete: need suggestions for attributes



#Student class: attributes: name, e, d, n
#name can possibly be used when creating pickle files to store individ. student's stuff?
class Student():
    def __init__(self, name,  e = "", d = "", n = ""):
        self.name = name
        self.e = e
        self.d = d
        self.n = n

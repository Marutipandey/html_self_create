"""class person():
    def __init__(self,lname,fname):
        self.ln=lname
        self.fn=fname
    def ho(self):
        print("hiiiiiiii",self.ln,self.fn)
col=person("sonam","poonam")
col.ho()
class per(person):
    pass
co=per("radhika","mohan")
co.ho()"""


class person():
    def __init__(self,lname,fname):
        self.ln=lname
        self.fn=fname
    def ho(self):
        print("hiiiiiiii",self.ln,self.fn)
col=person("sonam","poonam")
col.ho()
class per(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname)
co=per("radhika","mohan")
co.ho()
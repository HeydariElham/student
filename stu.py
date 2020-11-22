class student(person):
    def __init__(self,firstName,lastName,Id,nomre,dars):
        self.d = {}
        person.__init__(self,firstName,lastName,Id)
        self.d['nomre'] = nomre
        self.d['dars'] = dars
    def get_stu(self):
        return self.d

    def show_data(self):
        print(self.firstName,self.lastName,self.Id)
    

class person:
    def __init__(self,firstName,lastName,Id):
        self.d = {}
        self.d['firstName'] = firstName
        self.d['lastName'] = lastName
        self.d['Id'] = Id

class student(person):
    def __init__(self,firstName,lastName,Id,nomre,dars):
        self.d = {}
        person.__init__(self,firstName,lastName,Id)
        self.d['nomre'] = nomre
        self.d['dars'] = dars
    def get_stu(self):
        return self.d

    def get_dars(self):
        return self.d

    def del_dars(self):
        return self.d
    def show_cours(self):
        print("nomre:",self.nomre)
    
class employ(person):
    def __init__(self,firstName,lastName,Id,post):
       self.d = {}
       person.__init__(self,firstName,lastName,Id)
       self.d['post'] = post
    def get_emp(self):
        return self.d

class teacher(person):
    def __init__(self,firstName,lastName,Id,nomre):
      self.lst = []
      self.d = {}
      person.__init__(self,firstName,lastName,Id)
      self.d['nomre'] = nomre
      
    def get_teach(self):
        return self.d
    def show_cours(self):
        print("nomre:",self.lst)
    def edit_nomre(self):
        return
    def show_stu(self):
        return self.lst


lst = []
st1=student("mahsa","abdi",123,20,"dadeh")
st2=student("ali","hasani",234,18,"dadeh")
st3=student("hasan","karimi",456,19,"dadeh")
lst.append(st1.get_stu())
lst.append(st2.get_stu())
lst.append(st3.get_stu())
print(lst)

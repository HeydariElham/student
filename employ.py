class employ(person):
    def __init__(self,firstName,lastName,Id,post,salary):
       self.d = {}
       person.__init__(self,firstName,lastName,Id)
       self.d['post'] = post
       self.d['salary'] = salary
    def get_emp(self):
        return self.d
    def get_stu(self):
        return self.d
    def get_teach(self):
        return self.d
    def get_dars(self):
        return self.d

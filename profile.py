class profile(object):
    email = ""
    name = ""
    city = ""


    def __init__(self, email, name, city):
        self.email = email
        self.name = name
        self.city = city


    def to_csv(self):
        return self.email + "," \
               + self.name + "," \
               + self.city

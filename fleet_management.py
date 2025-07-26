class company:
    def __init__(self,name, address):
        self.name = name
        self.bus = []
        self.routes = []
        self.driver = []
        self.counter = []
        self.manager = []
        self.supervisors = []
        self.fare = []


class driver:
    def __init__(self, name, license, age):
        self.license = license
        self.name = name
        self.age = age

class counter:
    def __init__(self):
        pass

    def purchase_a_ticket(self, start, destination):
        pass
class passenger:
    pass

class supervisor:
    pass

nahid = driver('nahid',123,25)

        

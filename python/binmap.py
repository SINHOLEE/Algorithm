class Person:
    def __init__(self, m_id, name):
        self.m_id = m_id
        self.name = name

class Map:

    def __init__(self):
        self.arr = []

    
    def insert(self, p):
        self.arr.append(p)
        return True

    def print_list(self):
        for p in self.arr:
            print(p.m_id, p.name)

m = Map()

m.insert(Person(1, "sinho"))
m.insert(Person(2, "hh"))
m.print_list()


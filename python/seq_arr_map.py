class Person:
    def __init__(self, m_id, name):
        self.m_id = m_id
        self.name = name
    
    def set_idx(self, idx):
        self.idx = idx
    
    def __repr__(self):
        return "아이디: %s, 이름: %s, 인덱스: %s" % (self.m_id, self.name, self.idx)

class Map:

    def __init__(self):
        self.arr = []
        self.m_len = 0

    def insert(self, p):
        p.set_idx(self.m_len)
        self.arr.append(p)
        self.m_len += 1
        return True
    
    def find(self, key):
        target_idx = self._find_idx(key)
        return self.arr[target_idx]
        
    def _find_idx(self, key):
        for p in self.arr:
            if p.m_id == key:
                return p.idx
        return None

    def remove(self, key):
        target_idx = self._find_idx(key)
        if target_idx is not None:
            self.arr.pop(target_idx)  # O(n) 
        else:
            print("삭제불가")

    def print_list(self):
        for p in self.arr:
            print(p.m_id, p.name)

    

m = Map()

m.insert(Person(1, "sinho"))
m.insert(Person(2, "hh"))
m.print_list()

m.remove(1)
m.print_list()
class Person:
    def __init__(self, m_id, name):
        self.m_id = m_id
        self.name = name
    
    def __repr__(self):
        return "아이디: %s, 이름: %s" % (self.m_id, self.name)

class Map:
    def __init__(self):
        self.arr = [None] * 10
        self.m_len = 0
        self.size = 10

    def insert(self, p):
        if self.size > self.m_len:
            self.arr[self.m_len] = p
            self.m_len += 1
            return True
        else:
            return False
    
    def find(self, key):
        target_idx = self._find_idx(key)
        return self.arr[target_idx]
        
    def _find_idx(self, key):
        for i in range(self.m_len):
            if self.arr[i].m_id == key:
                return i
        return None

    def remove(self, key):
        target_idx = self._find_idx(key)
        if target_idx is not None:
            return self.remove_at(target_idx) 
        else:
            print("key: %s 삭제불가" % key)

    def remove_at(self, target_idx):
        for i in range(target_idx+1, self.m_len):
            self.arr[i-1] = self.arr[i]
        self.m_len -=1
        return True

    def print_list(self):
        print("self.m_len: %s " % self.m_len)
        print(self.arr)
        for i in range(self.m_len):
            print(self.arr[i])

    

m = Map()

m.insert(Person(1, "sinho"))
m.insert(Person(2, "a"))
m.insert(Person(4, "b"))
m.insert(Person(7, "c"))
m.insert(Person(3, "d"))
# m.print_list()

m.remove(6)
m.remove(7)
m.insert(Person(10, "10"))
m.insert(Person(10, "a"))
m.print_list()
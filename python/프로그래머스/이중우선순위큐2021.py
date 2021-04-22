import random
import time
import heapq
class Heap:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.max_deleted = {}
        self.min_deleted = {}
    def push(self, number):
        heapq.heappush(self.max_heap, -number)
        heapq.heappush(self.min_heap, number)
    def pop_min(self):
        if len(self.min_heap) > 0:
            number = heapq.heappop(self.min_heap)
            while number in self.min_deleted:
                self.min_deleted[number] -= 1
                if self.min_deleted[number] == 0:
                    del self.min_deleted[number]
                if len(self.min_heap) > 0:    
                    number = heapq.heappop(self.min_heap)
                else:
                    return None
            if number in self.max_deleted:
                self.max_deleted[number] += 1
            else:
                self.max_deleted[number] = 1
            return number
        else:
            return None
    def pop_max(self):
        if len(self.max_heap) > 0:
            number = -heapq.heappop(self.max_heap)
            while number in self.max_deleted:
                self.max_deleted[number] -= 1
                if self.max_deleted[number] == 0:
                    del self.max_deleted[number]
                if len(self.max_heap) > 0:    
                    number = -heapq.heappop(self.max_heap)
                else:
                    return None
            if number in self.min_deleted:
                self.min_deleted[number] += 1
            else:
                self.min_deleted[number] = 1
            return number
        else:
            return None
    def max(self):
        number = self.pop_max()
        if number is not None:
            self.push(number)
        return number
    def min(self):
        number = self.pop_min()
        if number is not None:
            self.push(number)
        return number
def solution(operations):
    heap = Heap()
    for operation in operations:
        op, number = operation.split(' ')
        number = int(number)
        if op == 'I':
            heap.push(number)
        elif op == 'D':
            if number == 1:
                heap.pop_max()
            elif number == -1:
                heap.pop_min()
    min_number = heap.min()
    max_number = heap.max()
    if min_number is not None and max_number is not None:
        answer = [max_number, min_number]
    else:
        answer = [0,0]
    return answer




# # 8:57
# import random
# import heapq
# import time
# import itertools

class DoubleHeapq:
    def __init__(self):
        self._heapq = []
        
    def answer(self):
        if(not len(self._heapq)):
            return [0, 0]
        elif len(self._heapq)==1:
            return [self._heapq[0],self._heapq[0]]
        else:
            return [self._heapq[self.find_max_index()], self._heapq[0]]
    def prt(self):
        print(self._heapq)
    
    def heap_push(self, value):
        heapq.heappush(self._heapq, value)
    
    def min_pop(self):
        if len(self._heapq):
            heapq.heappop(self._heapq)
    def max_pop(self):
        if len(self._heapq):
            max_index = self.find_max_index()
            # 별의별 시도 다 하는중 여기서 시간이 많이 걸림
            # self._heapq = list(itertools.chain(self._heapq[:max_index],self._heapq[max_index+1:]))
            # self._heapq = [*self._heapq[:max_index],*self._heapq[max_index+1:]]
            # self._heapq = self._heapq[:max_index]+self._heapq[max_index+1:]
            self._heapq.pop(max_index)
            heapq.heapify(self._heapq)
    
    def find_max_index(self):
        max_index = self._find_max_index(0)
        print("-----")
        print(self._heapq)
        print(max_index)
        return max_index
    
    def _find_max_index(self, parent_idx):
        # 자식이 하나도 없을때
        if(parent_idx*2+1 > len(self._heapq)-1): # len(self._heapq)-1 : 마지막 인덱스
            return parent_idx
        # 자식이 하나일 때
        elif parent_idx*2+2> len(self._heapq)-1:
            return parent_idx*2+1
        # 자식이 둘일 때
        else:
            left_max_index = self._find_max_index(parent_idx*2+1)
            right_max_index = self._find_max_index(parent_idx*2+2)
            
            if(self._heapq[left_max_index]<=self._heapq[right_max_index]):
                return right_max_index
            else:
                return left_max_index
        
        
def solution1(operations):
    dhq =  DoubleHeapq()
    for op in operations:
        a, b = op.split(" ")
        if a=='I':
            dhq.heap_push(int(b))
        else:
            if b== '1':
                dhq.max_pop()
            else:
                dhq.min_pop()
                
    return dhq.answer()

# # print(solution(['I 1', 'I 2', 'I 3', 'I 4', 'I 5', 'I 6', 'I 7', 'I 8', 'I 9', 'I 10', 'D 1', 'D -1', 'D 1', 'D -1']))


def operations():
    
    n = 10000
    def random_int():
        return random.randint(-9999999,9999999)
    def random_op():
        rand = random.randint(1,4)
        if rand == 1:
            return 'D 1'
        elif rand == 2:
            return 'D -1'
        else:
            return 'I %d' % (random_int())
    return [random_op() for i in range(n)]



# for i in range(10):


#     op = operations()
#     sinho = solution1(op)
#     haksu = solution(op)

#     # print(op)
#     if(sinho==haksu):
#         print(op)

print(solution1(['I 9', 'I 5', 'I 1', 'I 10', 'I 8', 'I 3', 'I 7', 'D 1', 'I 4', 'D 1']))
print(solution(['I 9', 'I 5', 'I 1', 'I 10', 'I 8', 'I 3', 'I 7', 'D 1', 'I 4', 'D 1']))


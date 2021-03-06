# Array and List

[TOC]

## 배열 (Array)

### 배열의 정의

배열은 어떤 메모리 블록에 연속적으로 나열된 같은 유형의 변수 모음이다.

- 여러 데이터를 하나의 이름으로 그룹핑해서 관리하기 위한 자료구조
- 배열을 이용하면 하나의 변수에 여러  정보를 담을 수 있고, **반복문과 결합** 하면 많은 정보도 효율적으로 처리할 수 있다. 
- 배열 인덱스는 값에 대한 **유일무이한 식별자**
  - 리스트에서 인덱스는 몇 번째 데이터인가 정도의 의미를 가지는 것과 대비된다.



### 배열의 특징

- **크기가 정해져 있다 / 기능이 없다**
  - 이는 배열의 장점이자 단점으로 배열은 다른 자료구조의 좋은 부품으로 사용될 수 있다.
- `인덱스` 를 가지며, 엘리먼트의 인덱스는 변경되지 않는다.
  - 현실세계의 주민번호, 학급에서 학생에게 부여하는 번호와 같다.
- 유관 데이터를 메모리에 순차적으로 (인덱스) 나열할 수 있다.
- 인덱스를 활용하여 빠르게 검색이 가능하다.
  - 원소의 인덱스를 알고 있다면 find 연산의 시간복잡도는 **O(1)**이다.
- `cache hit` 의 가능성이 커져서 성능에 큰 도움이 된다.
- 인덱스를 이용하여 데이터를 가져오려면 데이터에 대한 인덱스 값이 고정되어야 한다. (삭제된 엘리먼트의 공간이 그대로 남는다. → `메모리의 낭비`)



### 배열의 한계

- 배열은 길이를 바꿀 수 없다. 가변 배열과 같이 길이가 변경 가능한 배열의 경우,
  - 기존의 배열은 그대로 두고,
  - 새로운 길이로 지정된 배열을 따로 할당 후 (메모리가 있는지 탐색 필요)
  - 데이터의 복사를 진행하고,
  - 기존의 배열을 삭제한다.
  - `총 3번의 작업` + `메모리 탐색` 이 필요하기 때문에 리소스 낭비가 크다.
- 위와 같은 한계를 해결하기 위해서 `linked list 자료형`을 활용할 수 있다. (탐색, 할당, 복사, 삭제 등의 리소스 낭비가 없다.)
- 배열은 인덱스에 따라서 값을 유지하기 때문에, 엘리먼트가 삭제되어도 빈자리(null)가 남게 된다. (불필요한 메모리 차지)
- 조건문을 통해서 빈 엘리먼트를 제외할 수 있으나, 조건문을 많이 사용하는 것은 좋지 않다.
- 삭제한 데이터를 뒤에 위치한 엘리먼트로 메꾸면, 데이터가 순서에 따라서 빈틈없이 연속적으로 위치하며 이를 list(리스트) 라고 한다.
- 인덱스가 중요한 경우는 배열을 사용, 인덱스가 중요하지 않은 경우에는 리스트를 사용한다.



### 배열의 시간복잡도

- 검색 : **O(1)**
- 삽입 : O(N)
- 삭제 : O(N)
  -  만약 배열의 원소 중 어느 원소를 삭제했다고 했을 때, 배열의 연속적인 특징이 깨지게 된다. 즉 빈 공간이 생기는 것이다. 따라서 삭제한 원소보다 큰 인덱스를 갖는 원소들을 `shift`해줘야 하는 비용(cost)이 발생하고 이 경우의 시간 복잡도는 **O(N)**이 된다. 





## 리스트 (List)

### 리스트의 정의

리스트란 같은 값이 한번 이상 존재할 수 있고 순서가 있는 일련의 값이 모여있는 추상적 자료형(Abstract Data Type)이다.  

- 리스트는 배열의 장점인 빠른 데이터 조회 대신, **빈틈없는 데이터 적재**라는 장점을 취한 데이터 스트럭쳐이다.



### 리스트의 특징

- 리스트 자료구조의 핵심은 엘리먼트들 간의 `순서`. 따라서 리스트를 다른 말로는 `시퀀스(sequence)` 라고도 부른다. 즉 **순서가 있는 데이터의 모임이** 리스트이다.
- 리스트에서 인덱스는 **몇 번째 데이터인가** 정도의 의미를 가진다.
  - 배열에서의 인덱스는 값에 대한 **유일무이한 식별자**
- 빈 엘리먼트는 허용하지 않는다.
- 순차성을 보장하지 못하기 때문에 `spacial locality` 보장이 되지 않아서 `cash hit`가 어렵다.
- 데이터 갯수가 확실하게 정해져 있고, 자주 사용된다면 array가 더 효율적이다.
- 리스트에 대한 효용은 어떤 언어를 사용하느냐에 따라서 달라진다. 특히 많은 언어가 리스트를 기본적으로 지원하기 때문에 리스트를 직접 구현하는 경우는 줄고 있다.
-  **리스트**는 고정된 크기 없이 **포인터**로 자료들을 연결하기에, 자유자재로 데이터의 크기를 바꿀 수 있다. 하지만 인덱스가 없으므로 배열보다 자료를 찾는데 더 오랜시간이 걸려 배열보다 느리다는 단점이 있다.



### 파이썬에서의 리스트

- 기본적으로 리스트를 제공하며, 배열은 제공하지 않는다.
- 파이썬에서는 리스트가 배열이다.
- 파이썬의 리스트는 크기가 가변적이고, 어떤 원소 타입이던 저장할 수 있다는 장점을 가진다. 대신 C의 array 보다 메모리를 더 많이 필요로 한다는 단점이 있다.





## 연결 리스트(Linked List)

### 연결 리스트의 정의

연결리스트란 각 노드가 연결되어 있는 방식으로 데이터가 저장돼 있는 추상적 자료형이다.  각각의 원소들은 자기 자신 다음에 어떤 원소인지만을 기억하고 있다. 

- 연결 리스트는 `동적 할당`을 이용하여 필요할 때마다 길이를 늘이고 줄릴 수 있다.
  
  - 동적 할당
  
    ```python
    컴퓨터 프로그래밍에서 실행 시간 동안 사용할 메모리 공간을 할당하는 것을 말한다. 사용이 끝나면 운영체제가 쓸 수 있도록 반납하고 다음에 요구가 오면 재할당을 받을 수 있다. 이것은 프로그램이 실행하는 순간 프로그램이 사용할 메모리 크기를 고려하여 메모리의 할당이 이루어지는 정적 메모리 할당과 대조적이다. 
    
    동적으로 할당된 메모리 공간은 프로그래머가 명시적으로 해제하거나 쓰레기 수집이 일어나기 전 까지 그대로 유지된다. C/C++와 같이 쓰레기 수집이 없는 언어의 경우, 동적 할당하면 사용자가 해제하기 전까지는 메모리 공간이 계속 유지된다. 동적 할당은 프로세스의 힙영역에서 할당하므로 프로세스가 종료되면 운영 체제에 메모리 리소스가 반납되므로 해제된다.
    
    # 힙 영역 : 힙(heap)은 C 언어나 자바와 같은 프로그래밍 환경에서 원시 자료형이 아닌 보다 큰 크기의 데이터를 담고자 동적으로 할당하는 메모리 공간을 지칭한다.
    ```

- 한 노드는 해당 노드의 `실제값(value)`과 다음 노드의 주소값이 담긴 `포인터(pointer)`로 구성돼 있다. 마지막 노드의 포인터는 `Null`값을 갖는다. 
- 연결 리스트는 `단일 연결 리스트(singly-linked list)`, `이중 연결 리스트(doubly-linked list)`, `원형 연결 리스트(circularly-linked list)`로 나뉜다.



### 단일 연결 리스트

#### 단일 연결 리스트의 특성

- 리스트에 들어가는 각 데이터 원소에는 리스트의 다음 원소에 대한 `연결고리(포인터 또는 레퍼런스)`가 들어있다.
- **머리(head)** : 리스트의 첫 번째 원소
- **꼬리(tail)** : 리스트의 마지막 원소. 연결고리는 비어 있거나 `null` 연결고리로 이어져 있다.
- 단일 연결 리스트에 있는 연결고리는 다음 노드를 가리키는 포인터나 레퍼런스로만 구성되기 때문에 앞으로만 종주할 수 있다.
  - 따라서 리스트를 완전 종주하려면 항상 첫 번째부터 시작해야 한다.
  - 리스트에 있는 모든 원소의 위치를 파악하기 위해서는 리스트의 첫 번째 원소에 대한 포인터나 레퍼런스가 있어야만 한다.
  - 이 포인터나 레퍼런스는 별도의 자료구조에 저장한다.



#### 노드의 생성

```python
class Node(object):
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
```



#### 리스트의 생성

```python
class LinkedList(object):
    
    # self.head를 통해 head node를 지정해준다.
    def __init__(self, head=None):
        self.head = head
        self.size = 0
    
    
    def size(self):
        return self.size
    
    
    def is_empty(self):
        return self.size == 0
    
class EmptyError(Exception):
    pass
```



#### 노드의 삽입

```python
def insert_front(self, item):  # 연결 리스트의 맨 앞에 새 노드 삽입
    if self.is_empty():  # 연결 리스트가 empty인 경우
        self.head = self.Node(item, None)  # head가 새 노드 참조
    else: # empty가 아닌 경우
        self.head = self.Node(item, self.head)  # head가 새 노드 참조
    self.size += 1

        
def insert_after(self, item, p):  # p가 가리키는 노드 다음에 새 노드 삽입
    p.next = SList.Node(item, p.next)  # 새 노드가 p 다음 노드가 됨
    self.size += 1
```

- `단일 연결 리스트`에서는 반드시 `head`를 추적해야 한다. 그렇지 않으면 언어에 따라 `가비지 컬렉터`에 의해 제거되거나 어딘가에서 길을 잃게 된다.
  - 따라서 새로운 원소를 첫 번째 원소 앞에 추가하거나 리스트의 첫 번째 원소를 제거할 때 리스트의 `head`에 대한 `포인터` 또는 `레퍼런스`를 갱신해야 한다.
- 단일 연결 리스트`에 있는 원소들은 다음 원소에 대한 연결고리를 통해서만 관리할 수 있기 때문에 리스트 중간에서 원소를 삽입 또는 삭제하려면 그 앞 원소의 연결고리를 수정해야 한다.
- 주어진 연결리스트에 한 요소를 추가하는 연산의 계산복잡성은 리스트가 n개 요소로 구성돼 있을 때 **O(1)**이 된다. 전체 요소의 인덱스를 변경할 필요 없이 추가할 노드가 가리키는 다음 위치(포인터)를 기존 연결리스트의 요소에 연결하고, 추가할 새로운 노드를 기존 연결리스트의 이전 요소로 정의하기만 하면 되기 때문이다. 



#### 노드의 삭제

```python
def delete_front(self):  # p가 가리키는 노드의 앞 노드 삭제
    if self.is_empty():  # empty인 경우 에러 처리
        raise EmptyError('Underflow')
    else:
        self.head = self.head.next  # head가 둘째 노드를 참조
        self.size -= 1

        
def delete_after(self, p):  # p가 가리키는 노드의 뒷 노드 삭제
    if self.is_empty():  # empty인 경우 에러 처리
        raise EmptyError('Underflow')
    t = p.next
    p.next = t.next  # p 다음 노드를 건너뛰어 연결
    self.size -= 1
```

-  주어진 연결리스트의 요소를 삭제하는 연산의 계산복잡성은 리스트가 n개 요소로 구성돼 있을 때 **O(1)**이 된다.



#### 노드 탐색

``` python
def search(self, target):
    p = self.head
    for k in range(self.size):
        if target == p.item:
            return k
        p = p.next
    return None
```

-  주어진 연결리스트의 특정 위치에 있는 요소값을 읽거나 바꾸는 Access 연산의 계산복잡성은 **O(n)**이다. 예컨대 k번째 위치에 있는 값을 읽으려면 k개의 요소를 읽어들여야 하기 때문이다. 



### 이중 연결 리스트

#### 이중 연결 리스트의 특성

- 단일 연결 리스트는 다음 노드의 레퍼런스만 가질 수 있기 때문에 삽입 및 삭제 시 반드시 이전 노드의 레퍼런스를 알아야 했으며, 오직 한쪽 방향으로만 탐색할 수 있기 때문에 반대 방향에 위치한 노드는 탐색할 수 없다는 단점이 있다.
- 이중 연결 리스트는 앞과 뒤, 양쪽에 레퍼런스를 가짐으로서 이러한 단점을 보완한다.
- 두 개의 레퍼런스를 요구한다는 단점이 존재한다.



#### 노드의 생성

```python
class Node(object):
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next
```

- 다음과 같이 이전 노드의 레퍼런스를 저장해 놓는다.





## 배열과 연결 리스트의 차이

### ArrayList

  - 내부적으로 데이터를 배열에서 관리하며 데이터의 추가, 삭제를 위해서 임시 배열을 생성해 데이터를 복사하는 방법을 사용한다.
  - 대량의 자료를 추가/삭제 하는 경우 그만큼 데이터의 복사가 많이 일어나게 되어 성능 저하가 발생
  - 중간에 데이터를 삽입하기 위해서는 연속된 빈 공간이 존재해야 한다.
  - 반면 **인덱스**를 가지고 있어서 한 번에 참조가 가능해 데이터 검색에 유리하다.

  **ArrayList**는 삽입과 삭제를 할 일이 없거나 배열의 끝에서만 하게 될 경우 유용하게 쓰일 수 있다. 원소에 대해 빠르게 접근할 수 있을 뿐만 아니라, 원소들이 메모리에 연속으로 배치해 있어 CPU 캐시 효율도 더욱 높다.



### LinkedList

  - 데이터를 저장하는 각 노드가 이전 노드와 다음 노드의 상태만 알고 있으면 된다.
  - ArrayList와 달리 데이터의 추가, 삭제시 불필요한 데이터의 복사가 없어 데이터의 추가, 삭제시에 유리하다.
  - 반면, 데이터 검색 시에는 처음부터 노드를 순회하기 때문에 성능상 불리하다.



### 메모리 할당

- `Array`에서 메모리는 Array가 선언되자 마자 Compile time에 할당되어 진다. 이것을 정적 메모리 할당이라고 한다.
- **Stack** 영역에 메모리 할당이 이루어진다.
- `LinkedList`에서 메모리는 새로운 node가 추가될 때 runtime에 할당되어 진다. 이것은 동적 메모리 할당이라고 한다.
- **Heap** 영역에 메모리 할당이 이루어진다.



### 시간복잡도

|                   작업                   | 배열 리스트 (Array List) | 연결 리스트 (Linked List) |
| :--------------------------------------: | :----------------------: | :-----------------------: |
|        이전 원소 / 다음 원소 찾기        |           O(1)           |           O(1)            |
|       맨 뒤에 원소 추가 / 삭제하기       |       O(1) or O(N)       |           O(1)            |
| 맨 뒤 이외의 위치에 원소 추가 / 삭제하기 |           O(N)           |           O(1)            |
|         임의의 위치의 원소 찾기          |           O(1)           |           O(N)            |
|               크기 구하기                |           O(N)           |       O(N) or O(1)        |



### 결론

- 삽입과 삭제가 빈번하다면 `연결 리스트`를 사용하는 것이 더 좋다.
- 데이터의 접근하는 게 중요하다면 `배열 리스트`를 사용하는 것이 좋다.
def first(inp_str):
    return 8<=len(inp_str)<=15

def second(inp_str):
    for char in inp_str:
        if (ord('A')<= ord(char)<=ord('Z')):
            pass
        elif (ord('a')<= ord(char)<=ord('z')):
            pass
        elif (ord('0')<= ord(char)<=ord('9')):
            pass
        elif char in ['~','!','@','#','$','%','^','&','*']:
            pass
        else:
            return False
    return True
            

def third(inp_str):
    cnt=set()
    for char in inp_str:
        if (ord('A')<= ord(char)<=ord('Z')):
            cnt.add(1)
        elif (ord('a')<= ord(char)<=ord('z')):
            cnt.add(2)
        elif (ord('0')<= ord(char)<=ord('9')):
            cnt.add(3)
        elif char in ['~','!','@','#','$','%','^','&','*']:
            cnt.add(4)
    
    return len(cnt)>=3

def fourth(inp_str):
    for i in range(len(inp_str)-3):
        s = inp_str[i]
        cnt=0
        for j in range(4):
            if(s==inp_str[i+j]):
                cnt+=1
        if cnt==4:
            return False
    return True
    
def fifth(inp_str):
    dic = {}
    for chr in inp_str:
        if dic.get(chr) is None:
            dic[chr]=1
        else:
            dic[chr]+=1
    max_value = [value for key, value in dic.items()]
    return max(max_value)<5
def solution(inp_str):
    answer = []
    if not first(inp_str):
        answer.append(1)
    if not second(inp_str):
        answer.append(2)
    if not third(inp_str):
        answer.append(3)
    if not fourth(inp_str):
        answer.append(4)
    if not fifth(inp_str):
        answer.append(5)
        
    
    return answer if len(answer) else [0]

print(solution('1'))
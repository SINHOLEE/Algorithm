string = '2+3*4/5'
s1 = ''
mystack = []
for s in range(len(string)):
    if string[s] == '+' or string[s] == '-' or string[s] == '*' or string[s] == '/':
        mystack.append(string[s])
    else:
        s1 += string[s]

while mystack:
    s1 += mystack.pop()
print(s1)
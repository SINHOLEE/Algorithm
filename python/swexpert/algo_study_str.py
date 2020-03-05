# word = 'asdfghjkla'
# word= list(word)
# # reverse

# for i in range(len(word)//2):
#     word[i], word[-1-i] = word[-1-i], word[i]
    


# print(''.join(word))

# print(ord('9')-ord('0'))

# # itoa

# num = int(123)

# def itoa(num):
#     st =''
#     while num != 0: 
#         digit = num % 10 
        
#         st = st + chr(digit + 48)
#         num = num // 10
    
#     s=''
#     for a in range(len(st)-1,-1,-1):
#         s = s + st[a]
#     return s

# print(itoa(num))

# KMP 알고리즘

p = 'sinsiho'

word = 'I am a super sinho WkdWkd masn sin ho sino sinsih o asinhow hhh'


for w in range(len(word)):
    print(w, word[w])

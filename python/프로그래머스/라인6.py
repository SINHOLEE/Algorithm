
def solution(directory, command):
    drec = {}
    # print(directory)
    for d in directory:
        temp = drec
        print(d.split('/'))
        for item in d.split('/')[1:]:
            if temp.get(item) is None:
                temp[item] = {}
            else:
                temp= temp[item]


    print(drec)
    answer = []
    return answer

print(
    solution(
[
"/",
"/hello",
"/hello/tmp",
"/root",
"/root/abcd",
"/root/abcd/etc",
"/root/abcd/hello"
],
[
"mkdir /root/tmp",
"cp /hello /root/tmp",
"rm /hello"
]
)
)
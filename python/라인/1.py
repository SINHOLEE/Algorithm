def solution(table, languages, preference):
    score_table = {}
    for tb in table:
        temp = tb.split()
        score_table[temp[0]] = [0,0,0,0,0,0]
        for i in range(1,6):
            score_table[temp[0]][6-i] = temp[i]
    score = {}
    for job, values in score_table.items():
        total = 0
        print(values)
        for i in range(len(languages)):
            if languages[i] in values:
                for j in range(1,6):
                    if languages[i] == values[j]:
                        break
                total += preference[i] * j
        score[job] = total            
    answer = []
    max_value = 0
    for key, value in score.items():
        if max_value <= value:
            max_value = value
    for key, value in score.items():
        if max_value == value:
            answer.append(key)
    answer.sort()
    return answer[0]

solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],["PYTHON", "C++", "SQL"],[7,5,5])


#["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]	["JAVA", "JAVASCRIPT"]	[7, 5]	"PORTAL"
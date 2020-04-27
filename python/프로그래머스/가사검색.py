from pprint import pprint


def search(query, my_dic):
    cnt = 0
    temp = my_dic
    for i in range(len(query)):
        if query[i] == '?':
            num_of_questionmark = len(query) - i
            if temp["last_nums"].get(num_of_questionmark) is None:
                return 0
            else:
                return temp["last_nums"][num_of_questionmark]
        else:
            if temp.get(query[i]) is None:
                return 0
            else:
                temp = temp[query[i]]


def insert(word, my_dic):
    len_word = len(word)
    temp = my_dic
    for i in range(len_word):
        if temp.get(word[i]) is None:
            temp[word[i]] = {}
            temp = temp[word[i]]
            if temp.get("last_nums") is None:
                temp["last_nums"] = {}
            if temp["last_nums"].get(len_word - i - 1) is None:
                temp["last_nums"][len_word - i - 1] = 1
            else:
                temp["last_nums"][len_word - i - 1] += 1
        else:
            temp = temp[word[i]]
            if temp["last_nums"].get(len_word-i-1) is None:
                temp["last_nums"][len_word - i - 1] = 1
            else:
                temp["last_nums"][len_word-i-1] += 1
    # print(my_dic)

    return my_dic


def solution(words, queries):
    global dic, reversed_dic
    dic = {}
    reversed_dic = {}

    for word in words:
        dic = insert(word, dic)
        reversed_dic = insert(word[::-1], reversed_dic)

    answer = []
    for query in queries:
        if len(query) * '?' == query:
            answer.append(sum(map(lambda x: 1 if len(x) == len(query) else 0, words)))
            continue
        if query[0] == '?':
            answer.append(search(query[::-1], reversed_dic))
        else:
            answer.append(search(query, dic))
    return answer


solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["?????", "????o", "fr???", "fro???", "pro?"])

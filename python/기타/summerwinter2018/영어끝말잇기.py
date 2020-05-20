def solution(n, words):
    answer = [0, 0]
    q = [(i, 1) for i in range(1, n+1)]
    words_set = set()
    s = 0
    pre_word = ""
    for word in words:
        idx, rnd = q[s % n]
        if word in words_set:
            answer = [idx, rnd]
            break
        words_set.add(word)
        if pre_word != "":
            if pre_word[-1] != word[0]:
                answer = [idx, rnd]
                break
        q[s%n] = (idx, rnd+1)
        s+=1
        pre_word = word
    return answer


solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])
solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])

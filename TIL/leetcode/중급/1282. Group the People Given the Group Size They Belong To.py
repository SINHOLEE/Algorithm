'''
dic = {
    ()
}

'''


class Solution:
    def groupThePeople(self, groupSizes):
        dic = {}
        for i, g_size in enumerate(groupSizes):
            if g_size in dic:
                dic[g_size].append(i)
            else:
                dic[g_size] = [i]
        result = []
        for key, item in dic.items():
            for j in range(0, len(item), key):
                result.append(item[j:j+key])
        return result

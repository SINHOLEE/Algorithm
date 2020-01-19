class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def is_time_valid(time_string):
        h, m, s = map(int, time_string.split(':'))
        return (0 <= h <= 24) and (0<= m <= 59) and (0<= s <= 60)

    @classmethod
    def from_string(cls, time_string):
        h, m, s = map(str, time_string.split(':'))
        t = cls(h, m, s)
        return t


time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')


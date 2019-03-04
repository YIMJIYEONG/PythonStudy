class Arr:
    num1 = 0
    num2 = 0
    num3 = 0
    tmp = 0

    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

# 크기비교함수

    def arrange_num(self):
        a = [self.num1, self.num2, self.num3]
        for i in range(0, len(a)-1):
            for j in range(i+1, len(a)):
                if j < len(a):
                    if j < 3 and a[i] < a[j]:
                        self.tmp = a[j]
                        a[j] = a[i]
                        a[i] = self.tmp
        self.num1 = a[0]
        self.num2 = a[1]
        self.num3 = a[2]

# 출력함수

    def print(self):
        print("num1", "num2", "num3")
        print(self.num1, self.num2, self.num3)


arr = Arr(-8, 100, 7)
arr.arrange_num()

print(arr.print())


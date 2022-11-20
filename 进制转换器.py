class changeNumSystem:
    def creatAlpha(self):
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def formatNums(self, numLst):
        alpha = changeNumSystem.creatAlpha(self)
        for i in range(len(numLst)):
            j = numLst[i]
            if str(j).isnumeric():
                if 0 <= j < 10:
                    numLst[i] = str(j)
                else:
                    if 10 <= j < 36:
                        numLst[i] = alpha[j - 10]
                    else:
                        numLst[i] = "(" + str(j) + ")"
            elif j.isalpha():
                numLst[i] = j.upper()
            else:
                raise TypeError(i, "项不是整数/字母")
        return numLst

    def decodeNum(self, numstr):
        alpha = changeNumSystem.creatAlpha(self)
        i = 0
        numstrlen = len(numstr)
        out = []
        while i < numstrlen:
            point = numstr[i]
            if point.isnumeric():
                out.append(int(point))
            elif point.isalpha():
                point = point.upper()
                out.append(alpha.index(point) + 10)
            elif point == "(":
                j = i + 1
                try:
                    if numstr[j] != ")":
                        addin = []
                        while numstr[j] != ")":
                            addin.append(numstr[j])
                            j += 1
                        addin = "".join(addin)
                        addin = int(addin)
                        out.append(addin)
                    i = j
                except IndexError:
                    print("反括号呢？")
            i += 1
        return out

    def toTen(self, s_old, num):
        out = 0
        num = str(num)
        num = changeNumSystem.decodeNum(self, num)
        s_old = int(s_old)
        lenNum = len(num) - 1
        for i in range(lenNum, -1, -1):
            out += s_old ** i * int(num[lenNum - i])
        return out

    def tenToOther(self, s_new, num):
        num = int(num)
        s_new = int(s_new)
        remainder = lambda a, b: a - (a // b) * b
        integer = num
        out = []
        while integer:
            res = remainder(integer, s_new)
            out.append(res)
            integer //= s_new
        out.reverse()
        return out

    def cage(
        self,
        word,
        suspectwords=[
            ("114514", "有homo(喜)"),
            ("1919810", "太臭了"),
            ("1145141919810", "又来这一出"),
            ("juicy", "我就知道()"),
        ],
    ):
        for a, b in suspectwords:
            if word == a:
                print(b)


def main():
    robot = changeNumSystem()
    cage = robot.cage
    s_old = input("初始进制")
    cage(s_old)
    num_old = input("初始数字")
    cage(num_old)
    s_fin = input("转换进制")
    cage(s_fin)
    a = robot.toTen(s_old, num_old)
    b = robot.tenToOther(s_fin, a)
    out = robot.formatNums(b)
    out = "".join(out)
    cage(out)
    print(out)


if __name__ == "__main__":
    while True:
        main()
